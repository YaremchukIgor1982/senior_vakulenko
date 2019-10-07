import random
import time
from pprint import pprint

from data.data_rare.genet_data import url


# def test_shop(app):
#     app.open(url + '/shop')
#     products = app.driver.find_elements_by_css_selector('.products li')
#     products_info = [app.genetify.get_Product_info(product) for product in products]
#     pages = [product_url['link'] for product_url in products_info]
#     product_items = [ (app.open(page),app.genetify.get_Product_Page_Info()) for page in pages]
#     pprint(product_items)


def test_buy_random_product(app):
    app.open(url + '/shop')
    products = app.driver.find_elements_by_css_selector('.products li')
    random_product = random.choice(products)
    selected_product = app.genetify.get_Product_info(random_product)
    app.scroll(random_product)
    pprint(selected_product)
    random_product.find_element_by_css_selector('.button.product_type_simple.add_to_cart_button.ajax_add_to_cart').click()
    time.sleep(3)
def test_cart_icon(app):
    icon = app.driver.find_element_by_css_selector('.qodef-cart-number')
    app.scroll(icon)
    mini_cart = app.driver.find_element_by_css_selector('.qodef-shopping-cart-dropdown>ul>li')
    print("Item in Cart " +mini_cart.text)

def test_Cart_info(app):
    icon = app.driver.find_element_by_css_selector('.qodef-cart-number')
    app.scroll(icon)
    app.driver.find_element_by_css_selector('.qodef-view-cart>span').click()
    time.sleep(3)
    app.driver.find_element_by_css_selector('.product-thumbnail a').get_attribute('href')
    name = app.driver.find_element_by_css_selector('.product-name a')
    link = name.get_attribute('href')
    price = app.driver.find_element_by_css_selector('.product-price span').text
    subtotal = app.driver.find_element_by_css_selector('.product-subtotal span').text
    pprint({'product':name.text,'link':link,'price':price,'subtotal':subtotal})



#
# def test_open_checkout(app):
#     app.driver.find_element_by_css_selector('.qodef-view-checkout>span').click()
#     time.sleep(3)
#     print(app.driver.find_element_by_css_selector('.shop_table .cart_item').text)
#
#
# def test_form(app):
#     fake = Faker()
#     app.driver.find_element_by_css_selector('#billing_first_name').send_keys(fake.name())
#     app.driver.find_element_by_css_selector('#billing_last_name').send_keys(fake.last_name() + 'last')
#     app.driver.find_element_by_css_selector('#billing_company').send_keys(fake.company())
#     app.driver.find_element_by_css_selector('#billing_email').send_keys(fake.email())
#     app.driver.find_element_by_css_selector('#billing_phone').send_keys(fake.msisdn())
#     app.driver.find_element_by_css_selector('#billing_address_1').send_keys(fake.address())
#     app.driver.find_element_by_css_selector('#billing_address_2').send_keys(fake.street_suffix())
#     app.driver.find_element_by_css_selector('#billing_city').send_keys(fake.city())
#     app.driver.find_element_by_css_selector('#billing_postcode').send_keys(fake.postcode())
#     time.sleep(5)
#     app.driver.find_element_by_css_selector('#payment_method_cod').click()
#     app.driver.find_element_by_css_selector('#terms').click()
#     app.driver.find_element_by_css_selector('#place_order').click()
#
#     time.sleep(3)
#     # print("Used data for Feedback :");
#     # pprint({'name': name, 'email': email, 'phone': phone, 'last_name': last_name, 'msg': message})
#
