import random
import time
from pprint import pprint

import faker
import requests
from faker import Faker

url = 'https://baconlending.com'
def test_links(app):
    app.driver.get(url)
    links = app.driver.find_elements_by_css_selector('a')
    linked = [{'name':link.text,'link':link.get_attribute('href')} for link in links]
    pprint(linked)
    # for l in linked:
    #      status= requests.get(l['link'])
    #      print(l,status.status_code)



# def test_news_letter(app):
#     app.driver.find_element_by_css_selector('._field-wrapper>input').send_keys(Faker().email())
#     time.sleep(3)
#     app.driver.find_element_by_css_selector("button[type='submit'").click()
#     time.sleep(3)
#
# def test_apply(app):
#     app.driver.get(url)
#     app.driver.find_elements_by_css_selector('.header-cta-btn.bacon-apply-btn')[0].click()
#     time.sleep(3)
# def test_empty_form(app):
#     form = app.driver.find_element_by_css_selector('.wpcf7-form')
#     form.find_element_by_css_selector('input[type="submit"]').click()
#     time.sleep(3)
#     print(form.find_element_by_css_selector('.wpcf7-response-output').text)
#
#
# def test_apply_form(app):
#     name = "test "+Faker().name()
#     email = Faker().email()
#     phone= Faker().msisdn()
#     month = random.randrange(1,24)
#     form = app.driver.find_element_by_css_selector('.wpcf7-form')
#     fields = form.find_elements_by_css_selector('input')
#     for field in fields:
#         named = field.get_attribute('name')
#         if named == 'full-name':
#             field.send_keys(name)
#         elif   named == 'email-address':
#             field.send_keys(email)
#         elif   named == 'telephone-number':
#             field.send_keys(phone)
#         elif   named == 'est-month-revenue':
#             field.send_keys(month)
#     pprint({'name':name,'email':email,'phone':phone,"month":month})
#     checks = form.find_elements_by_css_selector('.wpcf7-list-item')
#     random.choice(checks).click()
#     form.find_element_by_css_selector('input[type="submit"]').click()
#     time.sleep(3)
#     print(form.find_element_by_css_selector('.wpcf7-response-output').text)

