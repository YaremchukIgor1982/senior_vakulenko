import random
import time
from pprint import pprint

from data.data_rare.mng_data import url


def test_shop(app):
    app.open(url + '/moisturizing-style-cream-40.html')
    time.sleep(2)
    swatch = app.driver.find_elements_by_css_selector('.swatch-option')
    option = random.choice(swatch)
    app.scroll(option)
    option.click()
    print(option.text)
    add = app.driver.find_element_by_css_selector('#product-addtocart-button')
    add.click()

def test_cart_footer(app):
    time.sleep(5)
    footer_mini_cart = app.driver.find_element_by_css_selector('#footer-mini-cart')
    print(footer_mini_cart.find_element_by_css_selector('.fixed-cart-col.fixed-cart-summary').text)
def test_open_Main_cart(app):
    app.driver.find_element_by_css_selector('.action.showcart').click()
    app.driver.find_element_by_css_selector('#top-cart-btn-checkout').click()
    pprint("Page : {}".format(app.morrocana.check_Page()))
