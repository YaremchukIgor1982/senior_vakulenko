import time

import pytest
import requests
from assertpy import assert_that

from data.smashed.sm_data import url_new


# @pytest.mark.parametrize('url',url_new)
# def test_404_Ui(app,url):
#     app.open(url)
#     time.sleep(5)
#     redirect = app.driver.current_url
#     time.sleep(3)
#     print('Url ' +url,'Redirect is '+redirect)
#
# @pytest.mark.parametrize('url',url_new)
# def test_Back_404(url):
#     check = requests.get(url)
#     print('Url ' + url,'Response Status',check.status_code)
