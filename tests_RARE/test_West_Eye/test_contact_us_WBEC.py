import time
from pprint import pprint

from faker import Faker

url = "http://wbec.smashedmedia.guru"
def test_contactUs(app):
    interest = Faker().word(ext_word_list=None)
    email = Faker().email()
    message = Faker().paragraphs(nb=3, ext_word_list=None)
    app.open(url+'/contact/')
    app.wbec.fill_Contact_from(email,interest,message)
    app.wbec.click_to_Send_Form()
def test_alert(app):
    time.sleep(3)
    app.response_alert_WP_contact_form()
