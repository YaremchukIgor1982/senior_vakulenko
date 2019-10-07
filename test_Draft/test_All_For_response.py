import time
from pprint import pprint

import pytest
import requests

# all = [
#     'https://smashedmedia.com',
#     'https://endlessfrontierlabs.com',
#     'https://philsanimalrentals.com',
#     'https://graciebarracoralsprings.com',
#     'https://graciebarrabocaraton.com',
#     'http://moroccangoldseries.com/',
#     'https://mygenetify.com',
#     'https://jiffylubeorlando.com',
#     'https://jiffylubesuncoast.com',
#     'https://jiffylubetampabay.com',
#     'http://packagingsupplygroup.com'
# ]
# @pytest.mark.parametrize('url',all)
# def test_response_All(url):
#     response = requests.get(url,verify=True)
#     pprint({'name':url,'status':response.status_code,'headers':response.headers})
# def test_all_for_response(app,url):
#     app.open(url)
#     time.sleep(3)
#     app.fullpage_screenshot('{}.png'.format(str(url)))
from bs4 import BeautifulSoup

from data.oem import wheels


@pytest.mark.parametrize('oem',wheels)
def test_oem(oem):
    page= requests.get(oem)
    soup = BeautifulSoup(page.text, 'lxml')
    links = soup.find_all('img')
    hrefs = []
    print(oem)
    for l in links:
        hrefs.append(l['src'])
    for h in hrefs:
        sts = requests.get(h)

        print(h, sts.status_code)
