import time
from pprint import pprint

import requests
from bs4 import BeautifulSoup
url = 'https://strongcloser.com/'

# def test_sitemap():
#     page = requests.get(url)
#     soup = BeautifulSoup(page.text, 'lxml')
#     cats = soup.find(id='fws_5d35bc745b087')
#     links = cats.find_all('a')
#     hrefs = [{'name': l.text, 'link': l.attrs['href']} for l in links]
#     print('Page is ' + url, "Page title is ", )
#     pprint(hrefs)
def test_Ui_sitemap(app):
    app.open(url+'sitemap/')
    sitemap = app.driver.find_element_by_css_selector('#fws_5d35bc745b087')
    items = sitemap.find_elements_by_css_selector('li a')
    hrefs=[{"name":i.text,"href":i.get_attribute('href')} for i in items]
    for link in hrefs:
        app.open(link['href'])
        time.sleep(2)
    pprint(hrefs)