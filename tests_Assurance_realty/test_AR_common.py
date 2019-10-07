import json
import re
from pprint import pprint

import pytest
import requests
from bs4 import BeautifulSoup

from data.app_data import htaccess
from fixture import rest

dev = "assurancer.smashedmedia.guru"


def test_Pages_Lassie(rest):
   doc = rest.get_data(htaccess+dev).text
   links = rest.find_(in_=doc,item='a::attr(href)')
   pages = rest.get_all_pages_Info_over_Website(dev,links)
   urls = [rest.convert_dev_url(page) for page in pages]
   pprint([rest.get_Lassie_object(url)for url in urls])


def testAssure_Links_load(app,rest):
    doc = rest.get_data(htaccess + dev).text
    links = rest.find_(in_=doc, item='a::attr(href)').getall()
    anchors = app.assure.filtering_links_for_Internal_and_external(links,dev)
    for page in anchors['internal']:
        dev_url = rest.convert_dev_url(page)
        inner = rest.get_data(dev_url).text
        inner_links = rest.find_(in_=inner, item='a::attr(href)').getall()
        print('Page : '+page)
        pprint(inner_links)
        app.open(dev_url)
        app.fullpage_screenshot('{}.png'.format(app.driver.title),scroll_delay=1)


def test_Pages(rest):
    doc = rest.get_data(htaccess + dev).text
    links = rest.find_(in_=doc, item='a::attr(href)').getall()
    pages = rest.get_all_pages_Info_over_Website(dev, links)
    urls = [rest.convert_dev_url(page) for page in pages]
    for url in urls:
        reg_page = rest.get_data(url).text
        reg_inner_links = rest.find_(in_=reg_page, item='::attr(href)').getall()
        print('Page : ' + url)
        pprint(reg_inner_links)


def test_responssive(emulator,rest):
        doc = rest.get_data(htaccess + dev).text
        links = rest.find_(in_=doc, item='a::attr(href)').getall()
        anchors = emulator.assure.filtering_links_for_Internal_and_external(links, dev)
        for page in anchors['internal']:
            dev_url = rest.convert_dev_url(page)
            emulator.open(dev_url)
            emulator.fullpage_screenshot("mobile_{}.png".format(emulator.driver.title), scroll_delay=2)
