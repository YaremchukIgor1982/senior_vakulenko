import time
from pprint import pprint

import pytest

from selenium.webdriver.common.keys import Keys

from data.data_rare.mng_data import items, url


@pytest.mark.parametrize('item',items)
def test_search(app,item):
    app.open(url)
    app.morrocana.search.open_search()
    app.morrocana.search.send_Search_Query(item)
    time.sleep(3)
    post_links = [app.morrocana.search.result_from_dropdown_info(p)  for p in app.morrocana.search.get_Results_from_dropdown()  if app.morrocana.search.dropdown_search()]
    pprint ("results from dropdown : {}".format(post_links))
    app.morrocana.search.input().send_keys(Keys.ENTER)
    time.sleep(3)
    pprint("Page info :{}".format(app.morrocana.check_Page()))






