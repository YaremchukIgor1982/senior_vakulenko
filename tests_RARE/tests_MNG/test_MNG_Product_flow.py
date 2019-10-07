import random
import time
from pprint import pprint

from data.data_rare.mng_data import url


def test_shop(app):
    app.open(url)
    shop =app.driver.find_element_by_xpath('//span[contains(text(),"Shop")]')
    app.scroll(shop)
    categories = app.driver.find_elements_by_css_selector('.em-menu-link')
    random_category = random.choice(categories)
    random_category_title = random_category.text
    random_category.click()
    print("Random category clicked: {}".format(random_category_title))
    time.sleep(5)


def test_category_shop_page(app):
    pprint("Page : {}".format(app.morrocana.check_Page()))


def test_product_select_category(app):
    items = app.morrocana.get_Items()
    random_product = random.choice(items)
    app.scroll(random_product)
    random_select = app.morrocana.Item_in_category(random_product)
    pprint("Random product : {}".format(random_select))
    app.morrocana.click_Title_for_Open(random_product)


def test_product_page_open(app):
    pprint("Page : {}".format(app.morrocana.check_Page()))



def test_options(app):
    swatch = app.driver.find_elements_by_css_selector('.swatch-option')
    option = random.choice(swatch)
    app.scroll(option)
    option.click()
    print(option.text)


def test_product_data(app):
    item_from_single_page = app.morrocana.get_Product_Info_from_Page()
    pprint("Product on opened Page :".format(item_from_single_page))
    add = app.driver.find_element_by_css_selector('#product-addtocart-button')
    app.scroll(add)
    add.click()


def test_cart_footer(app):
    footer_mini_cart = app.driver.find_element_by_css_selector('#footer-mini-cart')
    print(footer_mini_cart.find_element_by_css_selector('.fixed-cart-col.fixed-cart-summary').text)

def test_open_Main_cart(app):
    app.driver.find_element_by_css_selector('.action.showcart').click()
    app.driver.find_element_by_css_selector('#top-cart-btn-checkout').click()
    pprint("Page : {}".format(app.morrocana.check_Page()))






