import pytest
from pybatfish.client.session import Session
from pybatfish.datamodel import *
from pybatfish.datamodel.answer import *
from pybatfish.datamodel.flow import *
from pybatfish.client.commands import *
import yaml



def load_yaml() -> list:
    """
    This function loads the nornir inventory yaml file containing global variables
    for all network devices and grabs the NTP Servers list.
    """
    
    with open("your/yaml/file", "r") as f:
        data = yaml.safe_load(f)
    prod_ntp_servers = data['ntp_servers']
    return prod_ntp_servers

    
def load_batfish() -> Session:
    """
    This function creates a batfish session and sets up a network and a snapshot.
    Returns the batfish session object.
    """
    SNAPSHOT_DIR = 'your/snapshot/dir'
    batfish = Session(host="ip")
    batfish.set_network('lab-network')
    batfish.init_snapshot(SNAPSHOT_DIR, name="snapshot", overwrite=True)
    return batfish

def get_device_names() -> list:
    """
    This function uses the batfish session to retrieve a list of device names.
    Returns the list of device names.
    """
    bf = load_batfish()
    result = bf.q.nodeProperties().answer().frame()
    hostnames = result['Node'].tolist()
    return hostnames  



class TestNTP:
    """
    This class contains the test cases to verify the NTP configurations on the devices.
    """
    @pytest.mark.parametrize(
            'device_name', get_device_names()
            )
  
  
    def test_ntp(self, pytestbf, device_name):
        """
        This test case verifies if the NTP servers configured on the devices match the 
        NTP servers specified in the yaml file.
        """
        prod_ntp_servers = load_yaml()
        df = pytestbf.q.nodeProperties().answer().frame()
        result = df[df['Node'] == f'{device_name}']
        device_ntp_servers = result['NTP_Servers'].tolist()
        assert set(prod_ntp_servers) == set(device_ntp_servers[0])
