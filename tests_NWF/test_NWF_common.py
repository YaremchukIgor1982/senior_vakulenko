import time
from pprint import pprint

import sys
import time
import numpy

from screen_recorder_sdk import screen_recorder
from faker import Faker

from data.app_data import htaccess

dev = "nwf.smashedmedia.guru/"


# def test_all_Links(rest):
#     doc = rest.get_data(htaccess + dev).text
#     links = rest.find_(in_=doc, item='a::attr(href)').getall()
#     internal = []
#     external = []
#     for l in links:
#         if dev in l:
#             internal.append(l)
#         elif l.startswith('/'):
#             internal.append('https://' + dev + l)
#         elif 'paypal' or 'vimeo' in l:
#             external.append(l)
#     for page in internal:
#         dev_p = rest.convert_dev_url(page)
#         inner = rest.get_data(dev_p).text
#         time.sleep(3)
#         inner_links = rest.find_(in_=inner, item='::attr(href)').getall()
#         print("+++++++++++++++++++++++++++++++++++++Page : "+page)
#         pprint(inner_links)
        # inn_links = []
        # for i in inner_links:
        #     name = rest.find_(in_=i, item='::text').getall()
        #     href = rest.find_(in_=i, item='::attr(href)').get()
        #     inn_links.append({'name': name, "href": href})
        # print("Page is     :  " + rest.find_(in_=inner, item='title::text').get())
        # pprint(inn_links)


# def test_all_Butons(app, rest):
#     doc = rest.get_data(htaccess + dev).text
#     links = rest.find_(in_=doc, item='a::attr(href)').getall()
#     internal = []
#     external = []
#     for l in links:
#         if dev in l and l not in internal:
#             internal.append(l)
#         else:
#             external.append(l)
#     for i in internal:
#         btns = rest.find_(in_=doc, item='.nectar-button').getall()
#         print(i)
#         for b in btns:
#             name = rest.find_(in_=b, item='::text').get()
#             href = rest.find_(in_=b, item='::attr(href)').get()
#             print("Buttons first case ",name, href)
#     for i in internal:
#         url = rest.convert_dev_url(i)
#         app.open(url)
#         btns = app.driver.find_elements_by_css_selector('.nectar-button')
#         print("Page Ui : " + app.driver.title)
#         for b in btns:
#             app.scroll(b)
#             pprint({'href': b.get_attribute('href'), 'title': b.text, 'dimensions': b.size})
# #
#
#
def test_Contact(app):
    app.open(htaccess + dev + '/contact-us')



    # name = Faker().first_name()
    # company = Faker().company()
    # phone = Faker().msisdn()
    # email = Faker().email()
    # sentence = Faker().sentence()
    # app.contact.to_input('[name="your-name"]').send_keys(name)
    # app.contact.to_input('[name="your-company"]').send_keys(company)
    # app.contact.to_input('[name="your-phone"]').send_keys(phone)
    # app.contact.to_input('[name="your-email"]').send_keys(email)
    # app.contact.to_input('[name="your-message"]').send_keys(sentence)
    # app.driver.save_screenshot('filled_form.png')
    app.contact.button_Submit().click()
    time.sleep(5)
    resp = app.contact.response_WPCF_7()
    app.scroll(resp)
    app.driver.save_screenshot('response.png')