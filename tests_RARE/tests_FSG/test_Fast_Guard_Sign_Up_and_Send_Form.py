import random
import time
from pprint import pprint

from faker import Faker
from selenium.webdriver.common.keys import Keys
rang=random.randrange(2,7)

def test_Apply_Now_Sign_Up_User(app):
    app.open("https://fastguardservice.com/security-guard-jobs-near-me/")
    time.sleep(2)
    app.driver.find_element_by_css_selector('#cookie_action_close_header').click()
    time.sleep(5)
    app.driver.find_element_by_css_selector('.reg-form-buttons .lrm-register').send_keys(Keys.ENTER)
    app.efl.sign_up()

def test_apply_Apply_form(app):
    for i in range(8):
        step = 'apply_' + str(i + 1) + '_step'
        getattr(app.guard, step)()
        print(step)
        if step == 'apply_8_step':
            app.contact.button_Send_Form().click()
        else:
            app.scroll(app.efl.button_Next())
            app.efl.button_Next().send_keys(Keys.ENTER)
    # print(app.contact.response_WPCF_7())
    time.sleep()
    app.driver.delete_all_cookies()

#
# def test_Save_and_resume(app):
#     app.open("https://fgs.smashedmedia.guru/job-application/")
#     time.sleep(2)
#     app.driver.find_element_by_css_selector('#cookie_action_close_header').click()
#     time.sleep(5)
#     app.driver.find_element_by_css_selector('.reg-form-buttons .lrm-register').send_keys(Keys.ENTER)
#     app.efl.sign_up()
#     time.sleep(5)
#     print(rang)
#
# def test_fill_and_save_then_resume(app):
#     for i in range(rang):
#         step = 'apply_' + str(i + 1) + '_step'
#         getattr(app.guard, step)()
#         print(step)
#         if step == 'apply_'+str(rang)+'_step':
#             app.contact.button_Save().send_keys(Keys.ENTER)
#             time.sleep(3)
#             app.browser_alert('accept')
#         elif step!='apply_1_step':
#             time.sleep(2)
#             app.efl.button_Next().click()
#     app.driver.refresh()
#     time.sleep(10)
#     for i in range(1,rang):
#         for l in app.contact.labels():
#               print("Step {}".format(i))
#               pprint(app.contact.labels_info(l))
#               app.efl.button_Next().send_keys(Keys.ENTER)
#
#
#

