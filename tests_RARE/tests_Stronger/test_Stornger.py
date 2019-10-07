import random
import time
from pprint import pprint

import pytest
import requests
from bs4 import BeautifulSoup
from faker import Faker
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

dev = 'https://strongcloser.com/'

uris = [
    '/',
    '/category/current-issue/',
    '/about/',
    '/contact-us/',
    '/subscribe/',
    '/resources/',
    '/sales-career/',
    '/tools-training/',
    "/for-managers/",
    '/past-issues/'

]
acords = [
    '/for-managers/',
    '/tools-training/',
    "/sales-career/",
    '/past-issues/',
    '/resources/'

]


@pytest.mark.parametrize('uri',uris)
def test_accordeons(app,uri):
    app.open(dev+uri)
    table = app.driver.find_elements_by_css_selector('.toggles .toggle')
    for t in table:
        time.sleep(2)
        t.find_element_by_css_selector('h3 a').click()
        article = t.find_element_by_css_selector('.articles-link li a')
        pprint({'title':t.text,"article":article.get_attribute('href')})
        time.sleep(2)

@pytest.mark.parametrize('uri',uris)
def test_links(app,uri):
    app.open(dev+uri)
    all_links = app.driver.find_elements_by_css_selector('a')
    hrefs =[{link.get_attribute('href')} for link in all_links]
    print("page ",uri)
    pprint(hrefs)

def test_contact(app):
    app.open(dev + '/contact-us/')
    app.driver.find_element_by_css_selector('[name="your-name"]').send_keys(Faker().first_name())
    app.driver.find_element_by_css_selector('[name="phone"]').send_keys(Faker().msisdn())
    app.driver.find_element_by_css_selector('[name="your-email"]').send_keys(Faker().email())
    app.driver.find_element_by_css_selector('[name="text-41"]').send_keys(Faker().company())
    app.driver.find_element_by_css_selector('[name="your-message"]').send_keys(Faker().sentence())
    app.driver.find_element_by_css_selector('[name="Subject"]').click()
    opt = app.driver.find_elements_by_css_selector('option')
    randomed = random.choice(opt)
    randomed.click()
    print(randomed.text)
    app.driver.find_element_by_css_selector('[value="Submit"]').click()
    time.sleep(5)

def test_subscribe(app):
    app.open(dev)
    time.sleep(4)
    button = app.driver.find_element_by_css_selector('.nectar-button.subscribe-footer')
    button.click()
    app.driver.find_element_by_css_selector('input[name="your-email"]').send_keys(Faker().email())
    app.driver.find_element_by_css_selector('[value="Subscribe"]').click()
    time.sleep(3)

def test_Home(app):
    app.open(dev)
    post_area = app.driver.find_element_by_css_selector('.post-area')
    posts = post_area.find_elements_by_css_selector('.post-content')
    post_links = []
    for post in posts:
        app.scroll(post)
        post_links.append({"link": post.find_element_by_css_selector('a.entire-meta-link').get_attribute('href'),
                           'title': post.find_element_by_css_selector('h3.title').text})

    pprint(post_links)
    for link in post_links:
        app.open(link['link'])
        time.sleep(2)
        print("used ",link['link'],' ==>>>>',app.driver.current_url)

@pytest.mark.parametrize('uri', acords)
def test_links(uri):
    page = requests.get(dev + uri)
    soup = BeautifulSoup(page.text, 'lxml')
    links = soup.find_all('a')
    hrefs = [{'name': l.text, 'link': l.attrs['href']} for l in links]
    print('Page is ' + uri, "Page title is ", )
    pprint(hrefs)
