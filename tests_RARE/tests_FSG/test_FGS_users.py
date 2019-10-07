import json
import time

import pytest
from selenium.webdriver.common.keys import Keys

from data.stored import used
from fixture.file_manager import FileManager


# def test_Apply_Now_Sign_Up_User(ghost):
#     ghost.open("https://fgs.smashedmedia.guru/job-application/")
#     time.sleep(2)
#     ghost.driver.find_element_by_css_selector('#cookie_action_close_header').click()
#     time.sleep(5)
#     ghost.driver.find_element_by_css_selector('.reg-form-buttons .lrm-register').send_keys(Keys.ENTER)
#     user = ghost.efl.sign_up()
#     with FileManager('C:\\Users\Administrator\PycharmProjects\Scum\data\\users_data.json', 'r+') as f:
#         data = json.load(f)
#         data[user['user']]=user['email']
#     with FileManager('C:\\Users\Administrator\PycharmProjects\Scum\data\\users_data.json', 'w') as f:
#         json.dump(data,f)
#     print(f.closed)
def test_json():
    with open('C:\\Users\Administrator\PycharmProjects\Scum\data\\users_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        print(data.values())
        for d in data.values():
            if d=='kimberly27@mailinator.com':
                print(d)
