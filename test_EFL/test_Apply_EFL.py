import datetime
import random
import time
from pprint import pprint

import pytest
import requests
from faker import Faker
from selenium.webdriver.common.alert import Alert

from data.efl_data import dev_user, prod_user

dev = 'https://efl-dev.smashedmedia.guru'
prod = 'https://endlessfrontierlabs.com/'

# def test_forgot_password(app):
#     crushed = {'user': 'to_change_pass_account@mailinator.com', 'password': "Test123#"}
#     app.open(dev)
#     app.efl.menu_go_to('Apply Now')
#     app.driver.find_element_by_css_selector('.lrm-register').click()
#     app.efl.login_tab().click()
#     app.efl.logIn(crushed)
#
#     print(app.driver.find_element_by_css_selector('.lrm-form-message.lrm-form-message--init.lrm-is-error').text)
#     app.driver.find_element_by_css_selector('.lrm-switch-to--reset-password').click()
#     app.driver.find_element_by_css_selector('[name="user_login"]').send_keys(crushed['user'])
#     app.driver.find_element_by_css_selector('[name="user_login"]').submit()
#     time.sleep(2)
#     print("Got reset message " + app.driver.find_element_by_css_selector('.lrm-form-message').text)
#
# def test_Lost_your_password(app):
#     crushed = {'user': 'to_change_pass_account@mailinator.com', 'password': "Test123#"}
#     app.open(dev)
#     app.efl.menu_go_to('Apply Now')
#     app.driver.find_element_by_css_selector('.lrm-register').click()
#     app.efl.login_tab().click()
#     app.efl.logIn(crushed)
#     error = app.driver.find_element_by_css_selector('.lrm-form-message.lrm-form-message--init.lrm-is-error')
#     print(error.text)
#     error.find_element_by_css_selector('a').click()
#     time.sleep(2)
#     print(app.current())
#     app.driver.find_element_by_css_selector('#somfrp_user_info').send_keys(crushed['user'])
#     app.driver.find_element_by_css_selector('#somfrp_user_info').submit()
#     time.sleep(2)
def test_Apply_Now_Sign_Up_User(app):
    app.open(dev)
    app.efl.menu_go_to('Apply Now')
    app.driver.find_element_by_css_selector('.lrm-register').click()
    app.efl.sign_up()
    time.sleep(6)
    for i in range(10):
        step = 'apply_' + str(i + 1) + '_step'
        getattr(app.efl, step)()
        print(step)
        if step == 'apply_10_step':
            app.contact.button_Send_Form().click()
        else:
            time.sleep(2)
            app.efl.button_Next().click()

    time.sleep(20)

# def test_Apply_Now_Data_After_Send_by_New_User(app):
#     time.sleep(5)
#     for i in range(1, 10):
#         pprint([app.efl.labels_info(l) for l in app.efl.labels()])
#         if i != 10:
#             name = app.func_name()
#             app.catch_screen('efl', name)
#             app.efl.button_Next().click()
#
#
# def test_Login_User_on_Apply_Now(app):
#     app.open(dev)
#     app.efl.menu_go_to('Apply Now')
#     app.driver.find_element_by_css_selector('.lrm-register').click()
#     app.efl.login_tab().click()
#     app.efl.logIn(dev_user)
#     time.sleep(10)
#     for i in range(1, 10):
#         pprint([app.efl.labels_info(l) for l in app.efl.labels()])
#         if i != 10:
#             name = app.func_name()
#             app.catch_screen('efl', name)
#             app.efl.button_Next().click()
#
# def test_Apply_Now_Required_fields_and_Send_on_last_step(app):
#     app.open(dev)
#     app.efl.menu_go_to('Apply Now')
#     app.driver.find_element_by_css_selector('.lrm-register').click()
#     app.efl.sign_up()
#     time.sleep(6)
#     for i in range(10):
#         step = 'apply_' + str(i + 1) + '_step'
#         if step == 'apply_10_step':
#             getattr(app.efl, step)()
#             app.efl.button_Save().click()
#         elif step == 'apply_6_step' or step == 'apply_8_step':
#             getattr(app.efl, step)()
#             app.efl.button_Next().click()
#         else:
#             time.sleep(5)
#             app.efl.button_Next().click()
#             alerts = app.driver.find_elements_by_css_selector('.wpcf7-not-valid-tip')
#             for a in alerts:
#                 print(a.text," ","Field class ",a.find_element_by_xpath('..').get_attribute('class'))
#             getattr(app.efl, step)()
#             app.efl.button_Next().click()
#
#
