from pprint import pprint

import pytest
import requests
from bs4 import BeautifulSoup

dev = 'http://burganic.smashedmedia.guru/'
uris = [
       '/',
    'about',
    'menu',
    'organic',
    'contact-us',
    'menu-inner',
    'support-local',
    'menu-inner/?step=tab-burgers',
    'menu-inner/?step=tab-salads',
    'menu-inner/?step=tab-sweets'
]

@pytest.mark.parametrize('uri',uris)
def test_links(app,uri):
    app.open(dev+uri)
    links = app.driver.find_elements_by_css_selector('.nectar-button')
    hrefs=[]
    for l in links:
        app.scroll(l)
        href={"name":l.text,'inner_link':l.get_attribute('href')}
        hrefs.append(href)
    pprint({"page":uri,"buttons":hrefs})