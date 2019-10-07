import time
from pprint import pprint

from faker import Faker

from data.app_data import htaccess

dev = 'efl-dev.smashedmedia.guru'

def test_EFL_contact_form(app):
    app.open(htaccess+dev)
    app.efl.menu_go_to('Contact')
    app.efl.contact_form(name=Faker().name(), email='igory@smashedmedia.guru', message='Test Please ignore ' + Faker().sentence())
    time.sleep(2)
    app.contact.button_Submit().click()
    time.sleep(5)
    print(app.contact.response_WPCF_7())
    app.full_screen('efl_contact')


def test_newsletter(app):
    app.open(dev)
    email = Faker().email()
    app.efl.newsletter_proceed(email)
    time.sleep(3)
    print(email)