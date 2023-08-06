"""Pytest plugin that spins up the Flywheel integration test environment."""
# pylint: disable=redefined-outer-name
import logging
import os
import re
import socket
import typing as t
from functools import partial
from pathlib import Path

import docker
import pytest
import requests
from fw_core_client import CoreClient
from fw_utils import AttrDict
from memoization import cached
from retry.api import retry_call

from . import database
from .utils import get_db, get_defaults, merge

__all__ = ["_fw", "fw", "defaults", "pytest_configure"]


def get_docker_ip() -> str:  # pragma: no cover
    """Return the docker engine ip as accessible from host/containers alike."""
    # use the docker envvar if set (osx / ci)
    if DOCKER_HOST := os.getenv("DOCKER_HOST", ""):
        match = re.match(r"([^:/]+://)?(?P<host>[^:]+)(:\d+)?", DOCKER_HOST)
        assert match, f"Invalid DOCKER_HOST: {DOCKER_HOST}"
        return socket.gethostbyname(match.group("host"))
    # use the local machine's address (linux)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("8.8.8.8", 80))
    addr = sock.getsockname()[0]
    sock.close()
    return addr


DOCKER_IP = get_docker_ip()

MONGO_IMG = os.getenv("FW_MONGO_IMG", "mongo:4.4")
MONGO_RS = "elasticflywheel"
MONGO_RS_CONF = f"""
{{
  _id: "{MONGO_RS}",
  version: 1,
  members: [{{_id: 0, host: "{DOCKER_IP}:27017"}}]
}}
"""

# TODO make core version more easily configurable (for auto-updates)
# TODO warn if using latest (master) by default
CORE_IMG = os.getenv("FW_CORE_IMG", "flywheel/core-api:master")
STORAGE_URL = os.getenv("FW_STORAGE_URL", "osfs:///var/flywheel/data")
STORAGE_CREDS = os.getenv("FW_STORAGE_CREDS", "{}")
TEST_DATA_DIR = Path(os.getenv("FW_TEST_DATA_DIR", "tests/data")).resolve()

AUTH_CONFIG = """
auth:
  basic:
    enabled: true
"""

LOG_PATCH = """
from logging import StreamHandler
hdlr = StreamHandler()
LOG.logger.addHandler(hdlr)
log.logger.addHandler(hdlr)
""".lstrip().replace(
    "\n", "\\n"
)

CORE_CMD = f"""bash -euxc '
echo \"{AUTH_CONFIG}\" >auth.yaml;
sed -i "/^if __name__.*/i {LOG_PATCH}" bin/database.py
python bin/database.py wait_for_connection;
python bin/database.py upgrade_schema;
gunicorn -w 1 -c gunicorn_config.py web:app;
'
"""

client_info = dict(client_name="fw-test-env", client_version="dev")

log = logging.getLogger(__name__)


def pytest_configure(config):
    """Register custom fw_data marker."""
    config.addinivalue_line("markers", "fw_data(defaults): override defaults")


@pytest.fixture(scope="session")
def _docker():
    try:
        return docker.from_env()
    except docker.errors.DockerException:  # pragma: no cover
        return pytest.skip("Docker is not available, skipping test")


@pytest.fixture(scope="session")
def _network(_docker):
    name = "fw-net"
    net = _docker.networks.create(name)
    yield name
    net.remove()


@pytest.fixture(scope="session")
def _mongo(_docker, _network):
    name = "fw-mongo"
    cont = _docker.containers.run(
        MONGO_IMG,
        command=f"mongod --replSet {MONGO_RS}",
        ports={27017: 27017},
        detach=True,
        network=_network,
        name=name,
    )

    def init():
        status, output = cont.exec_run(f"mongo --eval 'rs.initiate({MONGO_RS_CONF})'")
        assert status == 0, f"mongo rs.initiate() exited with {status}:\n{output}"

    retry = dict(tries=3, delay=1, logger=log)
    retry_call(init, **retry)
    yield name
    cont.remove(force=True)


@pytest.fixture(scope="session")
def _core(_docker, _mongo, _network):
    name = "fw-core"
    url = f"http://{DOCKER_IP}:8080"
    db_url = f"mongodb://{DOCKER_IP}:27017"
    kwargs = {}
    if STORAGE_URL.startswith("osfs") and TEST_DATA_DIR.is_dir():
        # bind mount test data dir to `/var/flywheel/data/00/00`
        kwargs["volumes"] = {
            str(TEST_DATA_DIR): {"bind": "/var/flywheel/data/00/00", "mode": "rw"}
        }
    cont = _docker.containers.run(
        CORE_IMG,
        command=CORE_CMD,
        environment=dict(
            SCITRAN_AUTH_CONFIG_FILE="auth.yaml",
            SCITRAN_PERSISTENT_DB_URI=f"{db_url}/scitran?replicaSet={MONGO_RS}",
            SCITRAN_PERSISTENT_DB_LOG_URI=f"{db_url}/logs?replicaSet={MONGO_RS}",
            SCITRAN_PERSISTENT_FS_URL=STORAGE_URL,
            SYSLOG_HOST="localhost",
        ),
        ports={8080: 8080},
        detach=True,
        network=_network,
        name=name,
        **kwargs,
    )

    def init():
        requests.get(f"{url}/api/system").raise_for_status()

    try:
        retry = dict(exceptions=requests.ConnectionError, tries=15, delay=2, logger=log)
        retry_call(init, **retry)
    # pylint: disable=broad-except
    except Exception:  # pragma: no cover
        pytest.fail(f"Cannot connect to core. Logs:\n{cont.logs().decode()}")
    yield url
    cont.remove(force=True)


@pytest.fixture(scope="function")
def defaults(request):
    """Fixture that returns default data.

    Defaults can be overridden using the fw_data pytest marker.
    """
    marker = request.node.get_closest_marker("fw_data")
    defaults_ = get_defaults()
    if marker:
        defaults_ = merge(marker.args[0], defaults_)
    return AttrDict(**defaults_)


@pytest.fixture(scope="session")
def _fw(_core):
    """Session scoped pytest fixture that spins up the integration test environment."""
    db_url = f"mongodb://{DOCKER_IP}:27017/scitran?replicaSet={MONGO_RS}"
    file_size_fn = None
    if STORAGE_URL.startswith("osfs") and TEST_DATA_DIR.is_dir():
        file_size_fn = lambda f: Path(TEST_DATA_DIR, f).stat().st_size

    load = partial(
        database.load,
        core_url=_core,
        db_url=db_url,
        storage_url=STORAGE_URL,
        storage_creds=STORAGE_CREDS,
        file_size_fn=file_size_fn,
    )
    dump = partial(database.dump, db_url=db_url)
    reset = partial(database.reset, db_url=db_url)
    client = MagicCoreClient(_core, db_url)
    yield AttrDict(
        client=client,
        db_url=db_url,
        db=get_db(db_url),
        load=load,
        dump=dump,
        reset=reset,
        refs=database.refs,
        parents=database.parents,
    )


@pytest.fixture(scope="function")
def fw(_fw, defaults):
    """Function scoped fw pytest fixture with auto cleanup."""
    _fw.reset()
    _fw.load(defaults)
    yield _fw
    _fw.reset()


class MagicCoreClient:
    """Magic client to make easy initializing client for a given user."""

    def __init__(self, core_url: str, db_url: str):
        self.core_url = core_url
        self.db = get_db(db_url)  # pylint: disable=invalid-name

    def __getattr__(self, name: str) -> t.Any:
        api_key = self.db.apikeys.find_one({"_id": {"$regex": name}})
        if not api_key:
            raise AttributeError
        return get_client(self.core_url, api_key["_id"])


@cached
def get_client(core_url: str, api_key: str) -> CoreClient:
    """Get client with the given api-key."""
    return CoreClient(api_key=api_key, url=core_url, **client_info)
