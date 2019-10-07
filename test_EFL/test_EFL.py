import random
import time
from pprint import pprint

import pytest
import requests
from assertpy import assert_that
from bs4 import BeautifulSoup
from faker import Faker

dev = 'https://efl-dev.smashedmedia.guru'
uris = [
    '/',
    '/faq/',
    '/about/',
    '/tracks/',
    '/contact/',
    '/startups/',
    '/mentors/',
    '/apply-now/',
    '/deep-tech/',
    '/life-sciences/'

]
filters = [
    '.deep-tech-all-mentors',
    '.life-sciences-all-mentors',
    '.mentors',
    '.scientific-mentor'
    ]


def test_Home_content(app):
    app.open(dev)
    content = app.driver.find_elements_by_css_selector('.nectar-flip-box')
    for c in content:
        front = c.find_element_by_css_selector('.flip-box-front').text
        app.scroll(c)
        back = c.find_element_by_css_selector('.flip-box-back').text
        pprint({"front": front, "back": back})
    app.efl.swipe_slider()
    pprint(app.efl.check_slider_items())





@pytest.mark.parametrize('uri', uris)
def test_efl_Learn_More(app, uri):
    app.open(dev + uri)
    app.fullpage_screenshot('home.png'.format(str(uri)))
    learn_more = app.driver.find_elements_by_css_selector('.nectar-3d-transparent-button')
    for l in learn_more:
        app.scroll(l)
        time.sleep(3)


def test_empty_Contact_form(app):
    app.open(dev)
    time.sleep(3)
    app.efl.menu_go_to('Contact')
    app.efl.click_Submit_form()
    time.sleep(3)
    pprint(app.efl.alert_confirm())


#################################################################    need to be refactored

def test_Startups(app):
    app.open(dev)
    app.efl.menu_go_to('Startups')


    items = app.efl.work_items_grid()
    for i in items:
        app.scroll(i)
        print(i.find_element_by_css_selector('.work-item a').get_attribute('href'))


def test_Startups_open_Pop_up(app):
    app.open(dev + '/startups/')
    items = app.efl.work_items_grid()
    items[1].click()
    for i in range(1, 12):
        app.driver.find_element_by_css_selector('.mfp-arrow.mfp-arrow-right.mfp-prevent-close').click()
        time.sleep(3)
        print(app.driver.find_element_by_css_selector('.mfp-img').get_attribute('src'))

def test_Deep_tech_view_more_Startups(app):
    app.open(dev)
    app.efl.submenu_Tracks_go_to('Deep Tech')


    startups = app.driver.find_element_by_css_selector('.startups-row')
    app.scroll(startups)
    items = startups.find_elements_by_css_selector('img')
    pprint([{'img': item.get_attribute('src')} for item in items])
    button = startups.find_element_by_css_selector('a.deep-tech-local-startups')
    app.scroll(button)
    time.sleep(2)
    button.click()
    time.sleep(3)
    assert_that(app.driver.find_element_by_css_selector('a.active').text).is_equal_to('Deep Tech')
    print("Selected filter ", app.driver.find_element_by_css_selector('a.active').text)


def test_Life_scineces_view_more_Startups(app):
    app.open(dev)
    app.efl.submenu_Tracks_go_to('Life Sciences')


    startups = app.driver.find_element_by_css_selector('.startups-row')
    app.scroll(startups)
    items = startups.find_elements_by_css_selector('img')
    pprint([{'img': item.get_attribute('src')} for item in items])
    time.sleep(3)
    button = startups.find_element_by_css_selector('a.life-sciences-local-startups')
    app.scroll(button)
    button.click()
    time.sleep(3)
    print(app.driver.current_url)
    assert_that(app.driver.find_element_by_css_selector('a.active').text).is_equal_to('Life Sciences')
    print("Selected filter ", app.driver.find_element_by_css_selector('a.active').text)


def test_FAQ(app):
    app.open(dev + '/faq/')
    tabs = [app.efl.click_to_open_and_get_FaqItem_Info_close(p, t) for t in app.efl.table_FAQ() for p in
            app.efl.sub_table_FAQ(t)]
    pprint(tabs)


def test_Mentors_inner_PopUPs(app):
    app.open(dev)
    app.efl.menu_go_to('Mentors')
    grid = app.efl.work_items_grid()
    for mentor in grid:
        time.sleep(2)
        team = app.efl.mentor_info(mentor)
        mentor.click()
        time.sleep(1)
        opened = app.efl.mentor_pop_up_info()
        app.driver.find_element_by_css_selector('.mfp-close').click()
        print({'clicked':team['name'],'opened':opened})
#

