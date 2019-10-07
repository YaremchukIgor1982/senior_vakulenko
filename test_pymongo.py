import pandas as pd
from pprint import pprint

from faker import Faker
from pymongo import MongoClient

from fixture.mongo_db import MongoDBConnectionManager


# def test_one(app,mdb):
#     app.open('http://efl-dev.smashedmedia.guru/')
#     app.efl.menu_go_to('Apply Now')
#     app.driver.find_element_by_css_selector('.lrm-register').click()
#     user_name = Faker().word()
#     first_name = Faker().first_name()
#     last_name = Faker().last_name()
#     email = Faker().email('mailinator.com')
#     app.driver.find_element_by_css_selector('#signup-username').send_keys(user_name)
#     app.driver.find_element_by_css_selector('#signup-first-name').send_keys(first_name)
#     app.driver.find_element_by_css_selector('#signup-last-name').send_keys(last_name)
#
#     app.driver.find_element_by_css_selector('#signup-email').send_keys(email)
#     app.driver.find_element_by_css_selector('.fieldset--terms .lrm-nice-checkbox__indicator').click()
#     app.driver.find_element_by_css_selector(
#         '.lrm-signup-section .lrm-form .fieldset--submit button[type="submit"]').click()
#     user = ({'user': user_name, 'email': email})
#
#     edb= mdb.db('efl')
#     collection = edb.collection['sign_users']
#     collection.insert_one(user)
#
#
#     pprint([u for u in collection.find()])

def test_two(mdb):
    edb = mdb
    collection = edb.collection['mentors']
    edb.drop_collection(collection)