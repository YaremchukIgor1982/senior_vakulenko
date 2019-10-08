import time
from pprint import pprint

import requests
from assertpy import assert_that


def test_redirect(app, rest):
    global xl
    xl = []
    df = app.convert_from_excel('C:\\Users\Administrator\PycharmProjects\Scum\FastGuardURLRedirects.xls')

    for index, value in df.iterrows():
        xl.append({"old": value['Redirect broken URLS to --->'], 'new': value['new']})
# def test_rest():
#     for d in xl:
#         try :
#             page = requests.get(d['old'])
#             time.sleep(2)
#             pprint({"used":d['old'],"redirect_url":page.url})
#         except:
#             print('NOne')
def test_desktop(app):
    for d in xl:
        app.open(d['old'])
        time.sleep(3)
        assert_that(app.driver.current_url).is_equal_to(d['new'])
        if app.driver.current_url==d['new']:
           pprint({'old':d['old'],'redirect_to':app.driver.current_url})
        else :
            print('Not equal', d['old'])

