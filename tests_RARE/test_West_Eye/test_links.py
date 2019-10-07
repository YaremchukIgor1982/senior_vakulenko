from pprint import pprint

import requests
from bs4 import BeautifulSoup


def test_li():
    page = requests.get('https://wbec.smashedmedia.guru')
    soup = BeautifulSoup(*page, 'html')
    pprint(soup)

