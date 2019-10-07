from pprint import pprint

import pytest

from data.data_rare.mng_data import url, migrate


def test_sign_up(app):
    app.open(url+'/the-moroccan-way')
    links = app.driver.find_elements_by_css_selector('a')
    for l in links:
        pprint(l.get_attribute('href'))
    img = app.driver.find_elements_by_css_selector('img')
    for i in img:
        pprint(i.get_attribute('img'))

@pytest.mark.parametrize('old_url',migrate)
def test_migration(app,old_url):
    app.open(url + old_url)
    links = app.driver.find_elements_by_css_selector('a')
    hrefs = [l.get_attribute('href') for l in links]
    print(app.driver.current_url)
    pprint(hrefs)

