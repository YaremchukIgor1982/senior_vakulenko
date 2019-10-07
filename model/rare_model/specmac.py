from pprint import pprint

from faker import Faker
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class Spec():
    def __init__(self, app):
        self.app = app

    def header(self):
        return (self.app.driver.find_element_by_css_selector('#navbarCollapse'))

    def menu(self):
        menu = self.header().find_elements_by_css_selector('li.nav-item')
        return menu

    def menu_item(self, item):
        self.app.scroll(item)
        point = item.find_element_by_css_selector('a.nav-link')
        return ({'name': point.text, 'href': point.get_attribute('href')})

    def slider(self):
        return (self.app.driver.find_element_by_css_selector('#product-slider'))

    def product_gallery(self):
       products = self.slider().find_elements_by_css_selector('.owl-item .item')
       return products

    def slide_and_roll(self, p):
        move = ActionChains(self.app)
        move.click_and_hold(p).move_by_offset(50, 0).release().perform()

    def product_from_home(self, p):
        title = p.find_element_by_css_selector('h3')
        link = p.find_element_by_css_selector('a').get_attribute('href')
        print({'title': title.text, 'link': link})

    def contact_form(self):
        return(self.app.driver.find_elements_by_css_selector('.SendUsMessage input'))

    def input_data(self,contact_form,last,email,company,message):

        for f in contact_form:
            name = f.get_attribute('name')
            if name == 'first_name':
                f.send_keys('Smashed Media')
            elif name == 'last_name':
                f.send_keys(last)
            elif name == 'email':
                f.send_keys(email)
            elif name == 'phone':
                f.send_keys('(111)111-1111')
            elif name == 'company':
                f.send_keys(company)
                self.app.driver.find_element_by_css_selector('textarea').send_keys('Test Smashed Media Test ', message)
        pprint({'email': email, 'company': company})
    def submit_feedback(self):
        submit = self.app.driver.find_element_by_css_selector('.submit-section')
        submit.find_element_by_css_selector('.btn.mfg-btn').send_keys(Keys.ENTER)

    def alert(self):
        return(self.app.driver.find_element_by_css_selector('.alert'))

    def go_menu_to(self,str):
        menu = self.menu()
        item = filter(self.app.driver.find_element_by_link_text(str).click(), menu)
        return item

