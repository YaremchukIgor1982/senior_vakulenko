import time
from pprint import pprint
import re
import pandas as pd
from difflib import SequenceMatcher
from data.app_data import htaccess

url=''
dev = "regency.smashedmedia.guru/"
def test_meta(ghost):
    df = ghost.convert_from_excel('C:\\Users\Administrator\PycharmProjects\Scum\\test_RSS\RegencyShutterMetaData.xlsx')
    xl = []
    for index, value in df.iterrows():
        xl.append({"page": value['Web Page'], 'url': value['Web Page URL'], "meta title": value['Meta Title'],
                'meta description': value['Meta Description']})

    for x in xl:
        u_dev = x['url'].replace('https://regencyshutter.com/', dev, 1)
        ghost.open(htaccess+u_dev)
        time.sleep(3)
        meta_title = ghost.driver.title
        meta_description = ghost.driver.find_element_by_css_selector("meta[name='description']").get_attribute('content')
        site_data=({'title':meta_title,'meta_description':meta_description})

        title_ratio = SequenceMatcher(None, x['meta title'],site_data['title']).ratio()
        description = SequenceMatcher(None, x['meta description'],site_data['meta_description']).ratio()
        pprint({"page":x['url'],"equality title":title_ratio,"description equality":description})
