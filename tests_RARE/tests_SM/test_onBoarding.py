import random
import time
from pprint import pprint

from faker import Faker


def test_onboarding_form(app):
    fake=Faker()
    app.open('https://test.smashedmedia.com/onboarding')
    services = app.driver.find_elements_by_css_selector('.services .wpcf7-list-item')
    random_service = random.choice(services)
    random_service.find_element_by_css_selector('.checkbox-sign').click()
    print(random_service.text)
    app.driver.find_element_by_css_selector('.wpcf7-form-control.wpcf7-textarea').send_keys(fake.company()+' test')
    app.driver.find_element_by_css_selector('.your_business_name input').send_keys(fake.name())
    app.driver.find_element_by_css_selector('.your_business_title input').send_keys(fake.prefix_male())
    app.driver.find_element_by_css_selector('.phone input').send_keys(fake.msisdn())
    app.driver.find_element_by_css_selector('.email input').send_keys(fake.email())
    # app.driver.find_element_by_css_selector('.message textarea').send_keys(fake.message)
    app.driver.find_element_by_css_selector('.business_address input').send_keys(fake.street_suffix())
    app.driver.find_element_by_css_selector('.company_tag_line input').send_keys('test tag')
    app.driver.find_element_by_css_selector('.website input').send_keys(fake.hostname())
    # app.driver.find_element_by_css_selector('.message textarea').send_keys(fake.message)
    time.sleep(3)
    print("Used data for Feedback :")

