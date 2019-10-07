from pprint import pprint

from data.data_rare.genet_data import url


def test_home(app):
    app.open(url)
    slider = app.driver.find_elements_by_css_selector('.qodef-testimonial-content')
    for s in slider:
        app.scroll(s)
        quote = s.find_element_by_css_selector('.qodef-testimonial-text')
        author = s.find_element_by_css_selector('.qodef-testimonial-author')
        pprint({'Quote':quote.text,'author':author.text})
def test_products_onHome(app):
    products = app.driver.find_elements_by_css_selector('.qodef-pli-inner-holder')
    for p in products:
       app.scroll(p)
       link = p.find_element_by_css_selector('.qodef-pli-link').get_attribute('href')
       name_link =p.find_element_by_css_selector('.qodef-pli-link').get_attribute('title')
       data = p.find_element_by_css_selector('.qodef-pli-add-to-cart a')
       sku = data.get_attribute('data-product_sku')
       data_ide = data.get_attribute('data-product_id')
       qnty = data.get_attribute('data-quantity')
       href = data.get_attribute('href')
       name_ui = p.find_element_by_css_selector('.qodef-pli-text-wrapper a').text
       price_ui = p.find_element_by_css_selector('.qodef-pli-price  .woocommerce-Price-amount').text
       pprint({'link':link,'name_link':name_link,'sku':sku,'data_ide':data_ide,'qnty':qnty,'href':href,'name_ui':name_ui,'price_ui':price_ui})

def test_iwt(app):
    iwt_blocks = app.driver.find_elements_by_css_selector('.qodef-iwt')
    for i in iwt_blocks:
        title = i.find_element_by_css_selector('.qodef-iwt-content span').text
        tex = i.find_element_by_css_selector('.qodef-iwt-text').text
        pprint({'title':title,'text':tex})





