import random
import time

from pprint import pprint


import pytest
import requests
from bs4 import BeautifulSoup
from faker import Faker

from PIL import Image
dev = 'https://burganicburgers.com/'
uris = [
       '/',
    'about',
    'menu',
    'organic',
    'contact-us',
    'menu-inner',
    'support-local'
]
tabs = [
    'Burgers',
    'Salads',
    'Other',
]


@pytest.mark.parametrize('uri',uris)
def test_Page_UI(app,uri):
        app.open(dev+uri)
        if uri=='/':
                uri='home'
        app.fullpage_screenshot('{}.png'.format(str(uri)),scroll_delay=1)



def test_Join_Email(app):
        app.open(dev)
        app.driver.find_element_by_css_selector('[name="your-email"]').send_keys(Faker().email())
        app.driver.find_element_by_css_selector('[value="Submit"]').submit()
        time.sleep(2)
@pytest.mark.parametrize('uri',uris)
def test_Footer(app,uri):
        app.open(dev+uri)
        footer=app.driver.find_element_by_css_selector('#footer-widgets')
        app.scroll(footer)
        hours  = footer.find_elements_by_css_selector('#custom_html-6 .store_hours_footer li')
        socials = footer.find_elements_by_css_selector('#custom_html-7 .social_media_footer li a')
        menu = footer.find_elements_by_css_selector('#nav_menu-15 li a')
        nav =[{'menu': m.text, 'link': m.get_attribute('href')} for m in menu]
        work = [{'day': h.text} for h in hours]

        address = footer.find_element_by_css_selector('#text-6 .textwidget').text
        socials =[{'social': s.text, 'link': s.get_attribute('href')} for s in socials]
        print('Page '+app.driver.title)
        pprint({'address':address ,'shedule':work,'menu':nav,'socials':socials})

def test_Contact_form(ghost):
        ghost.open(dev +'contact-us/')
        time.sleep(3)
        ghost.contact.field('[value="Submit"]').click()
        time.sleep(3)
        ghost.contact.alert_required()
        print("Note " + ghost.contact.response_WPCF_7())
def test_Contact_Form_send(app):
        app.open(dev + 'contact-us/')
        app.contact.field('[name="your-name').send_keys(Faker().name())
        app.contact.field('[name="your-email').send_keys(Faker().email())
        app.contact.field('[name="your-message').send_keys(Faker().sentence())
        app.contact.field('[value="Submit"]').click()
        time.sleep(2)
        print("Note " +app.contact.response_WPCF_7())




