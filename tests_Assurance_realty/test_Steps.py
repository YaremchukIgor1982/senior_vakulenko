import time
from pprint import pprint

import pytest
from assertpy import assert_that

from data.app_data import htaccess
from tests_Assurance_realty.test_AR_common import dev

url = htaccess + dev
steps_pass={
    '2':'beFsRcTnLF',
    '3':'elC1oDfc41',
    '4':' n9vNSqy5nm',
    '5':'GhZLM6AZs6',
    '6':'DQEDfQ6uID',

}
@pytest.mark.parametrize("i",[1,2,3,4,5,6,7])
def test_Steps(app, rest,i):
    pages = []
    app.open(url + '/step-{}'.format(i))
    if 1 < i < 7:
        app.assure.unlock_step(i)
        pprint(app.driver.get_cookie('wp-postpass_85031b0725b210fc76700dc296362140'))

        app.fullpage_screenshot("{}.png".format(app.driver.title, scroll_delay=1))
        assert_that(app.driver.current_url).is_equal_to(
            "https://assurancer.smashedmedia.guru/step-{}-unlocked/".format(i))
        # info_url=app.driver.current_url.replace('https://',htaccess,1)
        pprint(rest.get_Lassie_object(url))
    # elif i == 1 or i == 7:
    #     app.fullpage_screenshot("{}.png".format(app.driver.title, scroll_delay=2))
    #     pages.append(app.driver.current_url)
    #     time.sleep(2)
        # info_url=app.driver.current_url.replace('https://',htaccess,1)
        # pprint(rest.get_Lassie_object(info_url))
# @pytest.mark.parametrize("i",[1,2,3,4,5,6,7])
# def test_locked_Steps(app,rest,i):
#
#     app.open(url + '/step-{}'.format(i))
#     app.fullpage_screenshot("{}.png".format(app.driver.title, scroll_delay=1))
#     pprint(rest.get_Lassie_object(url + '/step-{}'.format(i)))
# @pytest.mark.parametrize("step",[2,4,6])
# def test_steps_download(app,step):
#     app.open(url + '/step-{}'.format(step))
#
#     app.assure.unlock_step(step)
#     button = app.driver.find_elements_by_css_selector('a[text="Download Now"]')
#     if len(button)>0:
#         for b in button:
#             b.click()