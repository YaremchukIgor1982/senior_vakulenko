import time
from random import randint

import pytest
from faker import Faker
from selenium.webdriver.support.select import Select

from data.data_rare.gb_data import gb_urls

@pytest.mark.skip
@pytest.mark.parametrize('url',gb_urls)
def test_send_Start_Training(app,url):
    app.open(url)
    app.driver.find_element_by_css_selector('.qodef-btn-text').click()
    form = app.driver.find_element_by_css_selector('.qodef-side-menu')
    fake= Faker()
    form.find_element_by_css_selector('.customer-name>input').send_keys("Test_smashed _" + fake.first_name_male())
    form.find_element_by_css_selector('.customer-phone>input').send_keys(fake.msisdn())
    form.find_element_by_css_selector('.customer-email>input').send_keys(fake.email())
    classes = Select(app.driver.find_element_by_css_selector('.wpcf7-select'))
    classes.select_by_index(randint(0, len(classes.options)))
    app.driver.find_element_by_css_selector('.wpcf7-submit').click()
    time.sleep(3)


@pytest.mark.skip
@pytest.mark.parametrize('url',gb_urls)
def test_send_Feedback(app,url):
    app.open(url)
    fake = Faker()
    contact = app.driver.find_element_by_css_selector('.qodef-footer-top-holder .qodef-contact-form-7-widget')
    contact.find_element_by_css_selector('.your-name>input').send_keys("Test_smashed _"+fake.first_name_male())
    contact.find_element_by_css_selector('.your-email>input').send_keys(fake.email())
    contact.find_element_by_css_selector('textarea.wpcf7-textarea').send_keys("Test_smashed _" + fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None))
    contact.find_element_by_css_selector('.wpcf7-form-control.wpcf7-submit').click()
    time.sleep(5)
    print("Message from : {} ".format(url)+contact.find_element_by_css_selector('.wpcf7-response-output').text)

