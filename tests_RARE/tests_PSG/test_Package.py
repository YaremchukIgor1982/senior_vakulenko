from pprint import pprint

from faker import Faker
from selenium.webdriver.common.keys import Keys

dev_Url = 'http://packagingsupplygroup.com/'
def test_links(app):
    app.driver.get(dev_Url)
    links = app.driver.find_elements_by_css_selector('a')
    pprint([{'name':link.text,'href':link.get_attribute('href'),'target':link.get_attribute('target')} for link in links])

# def test_gallery(app):
#    product = app.driver.find_element_by_css_selector('.product_tabs')
#    tabs = product.find_elements_by_css_selector('.wpb_tabs_nav.ui-tabs-nav li a')
#    for tab in tabs :
#        app.scroll(tab)
#        tab.click()
#        gallery = product.find_element_by_css_selector('.left')
#        items = gallery.find_elements_by_css_selector('.wpb_wrapper')
#        items=[(app.scroll(i),{'title': i.find_element_by_css_selector('h4').text,'content': i.find_element_by_css_selector('p').text}) for i in items]
#
#        pprint({'tab':tab.text,'items':items})

def test_apply(app):
     email= Faker().email()
     message = Faker().paragraphs(nb=3, ext_word_list=None)
     form = app.driver.find_elements_by_css_selector('form.wpcf7-form input')
     for f in form:
             app.scroll(f)
             name = f.get_attribute('name')
             if name == 'your_name':
                 f.send_keys('Smashed Media')
             elif name == 'email':
                 f.send_keys(email)
             elif name == 'phone':
                 f.send_keys('(111)111-1111')
                 app.driver.find_element_by_css_selector('textarea').send_keys('Test Smashed Media Test ', message)
     app.driver.find_element_by_css_selector('.wpcf7-submit').send_keys(Keys.ENTER)
     app.driver.find_element_by_css_selector('.wpcf7-response-output')
     pprint({'email': email,"alert":app.driver.find_element_by_css_selector('.wpcf7-response-output').text})

