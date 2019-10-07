import re
import time

import pytest
from assertpy import assert_that

from data.smashed.sm_data import inner_services

#
# @pytest.mark.parametrize('service',inner_services)
# def test_sevices(app,rest,crawl,service):
#     service_page = rest.get_data(service)
#     soup = crawl.parser(service_page.text)
#     content =  soup.find('div',class_='inner-description').text
#     print(content)

    # doc = app.smashed.check_content_Services(service)
    # data = content.strip('\n')
    # print(data)
    # time.sleep(2)
    # assert doc in data