import time
from pprint import pprint

import requests
from assertpy import assert_that

url=''
dev = "regency.smashedmedia.guru/"
htaccess="user:HHoKdctSAHfmkgI1T6mv@"
def test_redirect(ghost,rest):

    df = ghost.convert_from_excel('C:\\Users\Administrator\PycharmProjects\Scum\\test_RSS\\UrlRedirects.xls')
    xl = []
    for index, value in df.iterrows():
        xl.append({"old": value['Old Site URLs redirect ---->'], 'new': value['to New Site URLs']})

    dev_links=[]
    for x in xl:
           u_dev = x['old'].replace('regencyshutter.com/',htaccess+dev, 1)
           dev_links.append(u_dev)

    for d in dev_links:
        try :
            page = requests.get(d)
            pprint({"used":d,"redirect":page.history,"redirect_url":htaccess+page.url})
        except:
            print('NOne')

