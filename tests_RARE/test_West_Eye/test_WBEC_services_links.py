import time
from pprint import pprint

import pytest
import requests

from data.wbec_data import services_old_url

url = "http://wbec.smashedmedia.guru"
# def test_dev_services(app):
#     app.open(url)
#     app.driver.find_element_by_css_selector('.section-down-arrow').click()
#     time.sleep(3)
#     links = app.driver.find_elements_by_css_selector('a.sm-service-link')
#     services = [(app.scroll(l),{'title':l.find_element_by_css_selector('.sm-service-title').text,
#                                 'href' : l.get_attribute('href')}) for l in links]
#     for service in services:
#         app.open(service[1]['href'])
#         inner_services = app.driver.find_elements_by_css_selector('.services_posts_shortcode .nectar-recent-post-slide')
#         inner_service_info = [(app.scroll(i),{'title':i.find_element_by_css_selector('h3 a').text,
#                                              'link':i.find_element_by_css_selector('a.blue-btn').get_attribute('href')})
#                                               for i in inner_services ]
#         print(service[1]['href'])
#         pprint(inner_service_info)
# # def test_prod_services(app):
# #     app.open('https://westbocaeyecenter.com/eye-conditions-expertise/')
# #     links = app.driver.find_elements_by_css_selector('.expertise>ul>li a')
# #     services = [(app.scroll(l),{'title':l.find_element_by_css_selector('span').text,
# #                                 'href' : l.get_attribute('href')}) for l in links]
# #     for service in services:
# #         app.open(service[1]['href'])
# #         inner_services = app.driver.find_elements_by_css_selector('article.type-service')
# #         inner_service_info_prod = [{'title':i.find_element_by_css_selector('h3 a').text,
# #                                              'link':i.find_element_by_css_selector('h3 a').get_attribute('href')}
# #                                               for i in inner_services ]
# #
# #         pprint({'page_url':service[1]['href'],'page':app.driver.title,'inners':inner_service_info_prod})
# @pytest.mark.parametrize('uri',services_old_url)
# def test_uri(app,uri):
#     app.open(url + uri)
#     time.sleep(2)
#     print('used : ' + uri,'page : '+app.driver.title,'current_url : '+app.driver.current_url)

def test_footer_links(app):
    app.open(url)
    footer= app.driver.find_element_by_css_selector('#footer-widgets')
    footer_links = footer.find_elements_by_css_selector('.widget_nav_menu li a')
    for f in footer_links:
        print(f.text,f.get_attribute('href'))