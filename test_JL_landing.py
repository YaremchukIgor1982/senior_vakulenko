import time
from pprint import pprint

from parsel import Selector

htaccess="https://user:HHoKdctSAHfmkgI1T6mv@"

def test_landing(app):
    app.driver.get(htaccess+'smashedmedia.guru/think-pink/')
    time.sleep(2)
    app.fullpage_screenshot('desktop_{}.png'.format(app.driver.title),scroll_delay=3)


def test_landing_mobile(emulator):
    emulator.driver.get(htaccess+'smashedmedia.guru/think-pink/')
    time.sleep(2)
    emulator.fullpage_screenshot('mobile_{}.png'.format(emulator.driver.title),scroll_delay=3)

def test_rest_Landos(rest):
    page = rest.get_data(htaccess+'smashedmedia.guru/think-pink/')
    sel = Selector(page.text)
    coupons = sel.css('.coupon-container').getall()
    for c in coupons:
        amount = rest.find_(in_=c, item='p::text').get()
        title = rest.find_(in_=c, item='.coupon-title::text').get()
        description = rest.find_(in_=c, item='.coupon-description::text').get()
        code = rest.find_(in_=c,item='.printomatic::attr(id)').get()
        pprint({'amount':amount,'title':title,'description':description,'print_id':code})

def test_Images_(rest):
    page = rest.get_data(htaccess+'smashedmedia.guru/think-pink/').text
    images = rest.find_(in_=page, item='img::attr(src)').getall()
    pprint(images)
