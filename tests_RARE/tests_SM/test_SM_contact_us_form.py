import time

import pytest
from faker import Faker

from data.app_data import Fake

url = 'https://smashedmedia.com/'
def test_contact_us_page(app):
     app.open(url)
     app.driver.find_element_by_css_selector('#menu-item-31177>a').click()
     time.sleep(2)
     app.smashed.contact_form( name='smashed'+Fake.name,last_name=Fake.last_name, email=Fake.email, phone=Fake.phone, message=Fake.message)
     name=app.func_name()
     app.catch_screen('smashed', name)
     app.driver.find_element_by_css_selector('.wpcf7-form-control.wpcf7-submit').click()
     time.sleep(3)
# def test_contact_Home(app):
#     app.open(url)
#     app.smashed.contact_form_Home( name='smashed_test'+Fake.name, email=Fake.email, website=Fake.website)
#     app.driver.find_element_by_css_selector('.wpcf7-form-control.wpcf7-submit').click()
#     time.sleep(5)
#     print(app.driver.title)