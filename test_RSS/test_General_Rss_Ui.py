import json
import random
import time
from collections import OrderedDict
from pprint import pprint

from data.app_data import htaccess

dev = 'regency.smashedmedia.guru/'



def test_responsive(app,rest):
    df = app.convert_from_excel('C:\\Users\Administrator\PycharmProjects\Scum\\test_RSS\\UrlRedirects.xls')
    xl = []
    for index, value in df.iterrows():
        xl.append({"page": value['Web Page'], 'url': value['Web Page URL']})
    for x in xl:
        u_dev = x['url'].replace('https://regencyshutter.com/', dev, 1)
        app.open(htaccess + u_dev)
        app.fullpage_screenshot("desktop_{}.png".format(app.driver.title),scroll_delay=0.5)
    for x in xl:
        w_dev = x['url'].replace('https://regencyshutter.com/', dev, 1)
        pprint(rest.get_Lassie_object(w_dev))