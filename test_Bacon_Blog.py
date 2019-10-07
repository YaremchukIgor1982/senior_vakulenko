from pprint import pprint

import allure
import pytest
from assertpy import assert_that


articles=[]

def test_Blog(rest):
    global articles
    page = rest.get_data('https://baconlending.com/blog/')
    posts = rest.find_(in_=page.text,item='article.post .content-inner').getall()
    articles=[]
    for post in posts:
        title = rest.find_(in_=post, item='h3 a::text').get()
        link = rest.find_(in_=post, item='h3 a::attr(href)').get()
        description = rest.find_(in_=post, item='.excerpt::text').get()
        date = rest.find_(in_=post, item='.text::text').get()
        articles.append({'title': title,'link':link, 'description': description, 'date': date})
    pprint(articles)
def test_Articles(app):
    for a in articles:
        app.open(a['link'])
        entry = app.driver.find_element_by_css_selector('h1').text
        # assert_that(a['title']).is_equal_to(entry)
        print(a,' ',app.driver.title)
        app.fullpage_screenshot('desktop2_{}.png'.format(entry),scroll_delay=2)
def test_emulator_Articles(emulator):
    for a in articles:
        emulator.open(a['link'])
        entry = emulator.driver.find_element_by_css_selector('h1').text
        # assert_that(a['title']).is_equal_to(entry)
        print(a,' ',emulator.driver.title)
        emulator.fullpage_screenshot('mobile2_{}.png'.format(entry),scroll_delay=2)