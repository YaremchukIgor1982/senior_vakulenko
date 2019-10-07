import time
from pprint import pprint

from haralyzer import HarParser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from data.app_data import htaccess
from fixture.bmp import ProxyManager

prod = 'https://endlessfrontierlabs.com/'
dev = 'efl-dev.smashedmedia.guru'
hta = 'https://user:HHoKdctSAHfmkgI1T6mv@'
def test_Updates(rest):
    global internal
    internal = []
    external = []
    doc = rest.get_data(hta+dev).text
    links = rest.find_(in_=doc, item='a::attr(href)').getall()
    for l in links:
        if dev in l and l not in internal:
            internal.append(l)
        else:
            external.append(l)

def test_parsed_inner_Page(rest):
    for i in internal:
        url = rest.convert_dev_url(i)
        pprint(rest.get_Lassie_object(url))
def test_Pages_to_open(emulator,rest):
    for i in internal:
         url = rest.convert_dev_url(i)
         emulator.open(url)
         emulator.fullpage_screenshot('mobile_{}.png'.format(emulator.driver.title),scroll_delay=2)
def test_har(bmp,rest):
    bmp.client.new_har(dev)
    for i in internal:
        url = rest.convert_dev_url(i)
        bmp.driver.get(url)
        bmp.driver.set_page_load_timeout(4)
        pprint(bmp.client.har)
    bmp.server.stop()




    har_parser = HarParser(bmp.client.har)
    print(har_parser.pages)