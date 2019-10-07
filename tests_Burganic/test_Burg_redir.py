from pprint import pprint

import pytest
import requests
from bs4 import BeautifulSoup

from data.burganic import redir


@pytest.mark.parametrize('old_link',redir)
def test_Migra(old_link):
    link = requests.get(old_link)
    html_doc = link.content
    soup = BeautifulSoup(html_doc)
    new_one = requests.get(link.url)
    pprint({"used_url_from_dev":old_link,'history':link.history,'redirect':link.url,
            'status_of_redirectedPage':new_one.status_code,'title':soup.title,})