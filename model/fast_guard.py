import datetime
import random
import time

from faker import Faker
from selenium.webdriver.common.keys import Keys
days=[
    '[name="sunday-shift-date"]',
    '[name="monday-shift-date"]',
    '[name="tuesday-shift-date"]',
    '[name="wednesday-shift-date"]',
    '[name="thursday-shift-date"]',
    '[name="friday-shift-date"]',
    '[name="saturday-shift-date"]'
]
class FGS:
    def __init__(self, app):
        self.app=app
        self.contact = app.contact

    def apply_1_step(self):
        time.sleep(5)
        self.contact.field('[name="application-name"]').send_keys(
            'QA SMashedMedia {}'.format(datetime.datetime.now()))
        self.contact.field('[name="application-phone"]').send_keys(Faker().msisdn())
        self.contact.field('[name="application-address"]').send_keys(Faker().street_address())
        self.contact.field('[name="application-city"]').send_keys(Faker().city())
        self.contact.field('[name="application-state"]').send_keys(Faker().state())


    def apply_2_step(self):
        time.sleep(3)
        self.contact.options_of('select[name="application-position-applied"]')
        self.contact.options_of('select[name="employment-type"]')
        self.contact.field('[name="available-start-date"]').send_keys('August 15, 2019 12:00 am')
        self.contact.field('[name="available-start-date"]').send_keys(Keys.ENTER)
        self.contact.field('[name="application-salary-expectations"]').send_keys(random.randint(500, 5000))

        for day in days:
            self.contact.options_of(day)



    def apply_3_step(self):
        time.sleep(2)
        self.contact.field('[name="application-computer-skills"]').send_keys(Faker().job())
        fields = self.contact.founders_blocks()
        for field in fields:
                inputs = field.find_elements_by_css_selector('input')
                for i in inputs:
                    name = i.get_attribute('name')
                    if name.startswith('institution-name-'):
                        i.send_keys(Faker().sentence(nb_words=6, variable_nb_words=True, ext_word_list=None))
                    elif name.startswith('degree-earned-'):
                        i.send_keys(Faker().suffix())
                    elif name.startswith('year-graduated-'):
                        i.send_keys(random.choice(['Yes',"No"]))
                    elif name.startswith('state-'):
                        i.send_keys(Faker().state())
                    elif name.startswith('city-'):
                        i.send_keys(Faker().city())
                    elif name.startswith('location-'):
                        i.send_keys(Faker().military_dpo())
                    elif name.startswith('certifications-name-'):
                        i.send_keys(Faker().license_plate())
        self.contact.field('[name="application-language-proficiency"]').send_keys(Faker().sentences())

    def apply_4_step(self):
        time.sleep(2)
        fields = self.contact.founders_blocks()
        for field in fields:
            fields_row = field.find_elements_by_css_selector('.field-founders')
            for field in fields_row:
                inputs = field.find_elements_by_css_selector('input')
                for i in inputs:
                    name = i.get_attribute('name')
                    if name.startswith('branch-'):
                        i.send_keys(Faker().company_suffix())
                    elif name.startswith('highest-rank-'):
                        i.send_keys(random.randint(1, 100))
                    elif name.startswith('years-served-'):
                        i.send_keys(Faker().year())
                    elif name.startswith('law-agency-'):
                        i.send_keys(Faker().company())
                    elif name.startswith('law-highest-rank-'):
                        i.send_keys(random.randint(1, 100))
                    elif name.startswith('law-years-served-'):
                        i.send_keys(Faker().year())
                    elif name.startswith('previouse-employer-'):
                        i.send_keys(Faker().company())
                    elif name.startswith('previouse-position-'):
                        i.send_keys(Faker().job())
                    elif name.startswith('previouse-location-'):
                        i.send_keys(Faker().city())
                    elif name.startswith('previouse-contact-employer-'):
                        i.send_keys(Faker().msisdn())

    def apply_5_step(self):
        time.sleep(2)
        radio=self.contact.form().find_elements_by_css_selector('.wpcf7-radio')
        for r in radio:
            vars = r.find_elements_by_css_selector('[type="radio"')
            random.choice(vars).click()

    def apply_6_step(self):
        time.sleep(2)
        self.contact.field('[name="application-customer-service-mean"]').send_keys(Faker().sentence())
        self.contact.field('[name="application-why-should-hire"]').send_keys(Faker().sentence())
        self.contact.field('[name="application-your-strengths"]').send_keys(Faker().sentence())
        self.contact.field('[name="application-your-weakness"]').send_keys(Faker().sentence())
        self.contact.field('[name="application-deal-with-difficult-customer"]').send_keys(Faker().sentence())
        self.contact.field('[name="application-handle-stress-pressure"]').send_keys(Faker().sentence())


    def apply_7_step(self):
        time.sleep(5)
        fields = self.contact.founders_block()
        for field in fields:
            fields_row = field.find_elements_by_css_selector('.field-founders')
            for field in fields_row:
                inputs = field.find_elements_by_css_selector('input')
                for i in inputs:
                    name = i.get_attribute('name')
                    if name.startswith("reference-name-"):
                        i.send_keys(Faker().name())
                    elif name.startswith('reference-position-'):
                        i.send_keys(Faker().job())
                    elif name.startswith('reference-company-'):
                        i.send_keys(Faker().company())
                    elif name.startswith('reference-phone-'):
                        i.send_keys(Faker().msisdn())


    def apply_8_step(self):
        time.sleep(5)
        self.contact.field('[name="application-signature-sign"]').send_keys("Igor QA")

        self.contact.field('[name="application-signature-sign"]').send_keys("[]".format(datetime.datetime.now()))


