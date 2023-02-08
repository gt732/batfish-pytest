import pytest
from pybatfish.client.session import Session
from pybatfish.datamodel import *
from pybatfish.datamodel.answer import *
from pybatfish.datamodel.flow import *
from pybatfish.client.commands import *


@pytest.fixture(scope="session")
def pytestbf():
    pytestbf = Session(host="ip")
    SNAPSHOT_DIR = 'your/snapshot/dir'
    pytestbf.set_network('lab-network')
    pytestbf.init_snapshot(SNAPSHOT_DIR, name="snapshot", overwrite=True)
    yield pytestbf
