import time
from pprint import pprint

from data.app_data import htaccess

dev = "nwf.smashedmedia.guru/"
def test_home(app):
    app.open(htaccess+dev)
    app.fullpage_screenshot('home.png',scroll_delay=3)

# def test_Layout(rest):
#     global internal
#     doc = rest.get_data(htaccess + dev).text
#     links = rest.find_(in_=doc, item='a::attr(href)').getall()
#     internal = []
#
#     external = []
#     for l in links:
#         if dev in l and l not in internal:
#             internal.append(l)
#         elif 'paypal' or 'vimeo' in l:
#             external.append(l)

#
# def test_page_by(emulator, rest):
#     for page in internal:
#         internal.append(htaccess + dev)
#         dev_url = rest.convert_dev_url(page)
#         emulator.open(dev_url)
#         emulator.fullpage_screenshot('mobile_{}.png'.format(emulator.driver.title), scroll_delay=3)



# def test_catch_all_Screens_by(app, rest):
#     for i in internal:
#         url = rest.convert_dev_url(i)
#         app.open(url)
#         app.fullpage_screenshot('desktop{}.png'.format(app.driver.title),scroll_delay=3)
#         print("Page Ui : " + app.driver.title)
# def test_header_footer_layout(app,rest):
#     for i in internal:
#         url = rest.convert_dev_url(i)
#         app.open(url)
#         time.sleep(3)
#         footer = app.driver.find_element_by_css_selector('#media_image-3')
#         app.scroll(footer)
#         time.sleep(3)
#         app.driver.save_screenshot('heaader_footer{}.png'.format(app.driver.title))
