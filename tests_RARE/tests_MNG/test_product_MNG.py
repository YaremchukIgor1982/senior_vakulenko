import time
from pprint import pprint

from data.data_rare.mng_data import url


def test_products(app):
    app.open(url)
    app.driver.find_element_by_xpath('//span[contains(text(),"Shop")]').click()
    items = app.morrocana.get_Items()
    print(len(items))
    products=[app.morrocana.Item_in_category(item) for item in items]
    page_links=[prod['link'] for prod in products]
    pprint(products)
    product = [(app.open(l),time.sleep(3), app.morrocana.get_Product_Info_from_Page()) for l in page_links]
    pprint(product)

