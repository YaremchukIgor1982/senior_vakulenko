from pprint import pprint

import pytest
import requests

from data.data_rare.gb_data import march_request


# @pytest.mark.parametrize('url',march_request)
# def test_migration(app,url):
#     app.open(url)
#     time.sleep(4)
#     assert app.driver.current_url == 'https://graciebarrabocaraton.com/'
#     pprint({'Used_url':url,'Redirect_url':app.driver.current_url})

@pytest.mark.parametrize('url', march_request)
def test_with_redirects_and_response_history(url):
    response = requests.get(url)
    assert response.url=='https://graciebarrabocaraton.com/'
    result = {'used_url':url,'response':response.history,'redirected_url':response.url}
    pprint(result)





