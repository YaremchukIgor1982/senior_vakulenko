import pytest
import requests

from data.app_data import htaccess
from data.smash_dev_server import smash_dev_server


@pytest.mark.parametrize('dev',smash_dev_server)
def test_Server_noPass(dev):
    instance = requests.get("https://"+dev)
    print({"autethication":"No","instance":dev,"status":instance.status_code})


@pytest.mark.parametrize('dev',smash_dev_server)
def test_Server_Pass(dev):
    instance = requests.get(htaccess + dev)
    print({"autethication": "Yes", "instance": dev, "status": instance.status_code})
