import random
from selenium.webdriver.support import expected_conditions as ec
from faker import Faker
from selenium.webdriver.support import wait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class ContactForm7:

    def __init__(self, app):
        self.app = app

    def form(self):
        return self.app.driver.find_element_by_css_selector('.wpcf7')

    def to_input(self,name):
        return self.form().find_element_by_css_selector(name)


    def field(self, name):
        return self.form().find_element_by_css_selector(name)

    def alert_required(self):
        alerts = self.form().find_elements_by_css_selector('.wpcf7-not-valid-tip')
        for a in alerts:
            print(a.text)
            print(a.find_element_by_xpath('..').get_attribute('class'))

    def button_Send_Form(self):
        return self.form().find_element_by_css_selector('[value="Send"]')

    def labels(self):
        instns = self.form().find_element_by_css_selector('.cf7mls_current_fs')
        return instns.find_elements_by_css_selector('label')

    def labels_info(self, f):
        self.app.scroll(f)
        return {'title': f.text,
                'info': f.find_element_by_css_selector('span .wpcf7-form-control').get_attribute('value')}

    def button_Save(self):
        return (self.form().find_element_by_css_selector('.cf7mls_current_fs a.btn-save-form'))

    def button_Restore(self):
        return (self.form().find_element_by_css_selector('.btn-restore-form'))

    def button_Submit(self):
        return (self.form().find_element_by_css_selector('[type="Submit"]'))

    def checkboxes(self,arg):
        return self.form().find_elements_by_css_selector('.founders-block input[value="{}"]'.format(arg))


    def response_WPCF_7(self):
        return (self.form().find_element_by_css_selector('.wpcf7-response-output'))

    def founders_block(self):
         return self.form().find_element_by_css_selector('.founders-block .container-fluid')

    def founders_blocks(self):
         return self.form().find_elements_by_css_selector('.founders-block .container-fluid')

    def dropdown(self):
        return self.form().find_element_by_css_selector('.select2-results__options ')

    def options_of(self,dropfield):
        select = self.form().find_element_by_css_selector(dropfield)
        all_options = select.find_elements_by_tag_name("option")
        del all_options[0]
        random.choice(all_options).click()