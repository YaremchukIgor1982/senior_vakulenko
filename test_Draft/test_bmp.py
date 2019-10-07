import json
import pprint
import time

from haralyzer import HarParser, HarPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from data.app_data import htaccess
from fixture.bmp import ProxyManager


def test_har():
    proxy = ProxyManager()
    server = proxy.start_server()
    client = proxy.start_client()
    client.new_har('regency.smashedmedia.guru/')

    print(client.proxy)
    chrome_options = Options()
    chrome_options.add_argument("--proxy-server={}".format(client.proxy))
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get(htaccess+'regency.smashedmedia.guru/')
    time.sleep(3)
    # pprint.pprint(client.har)
    server.stop()




    har_parser = HarParser(client.har)
    print(har_parser.pages)

