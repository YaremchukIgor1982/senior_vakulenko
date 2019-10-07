from pprint import pprint

import pytest
import requests
from bs4 import BeautifulSoup

from data.wbec_data import old_urls, except_urls, new

url = "http://52.35.36.109/"


@pytest.mark.parametrize('old_link',new)
def test_Migra(old_link):
    link = requests.get(old_link)
    html_doc = link.content
    soup = BeautifulSoup(html_doc)
    new_one = requests.get(link.url)
    pprint({"used_url_from_dev":old_link,'history':link.history,'redirect':link.url,
            'status_of_redirectedPage':new_one.status_code,'title':soup.title,})

#
# @pytest.mark.parametrize('old_link',old_urls)
# def test_Ui_redirects(app,old_link):
#     app.open(old_link)
#     pprint({'used url':old_link,'title':app.dri
#
# ver.title,'redirect_to':app.driver.current_url})