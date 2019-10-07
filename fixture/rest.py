import re
import time
from pprint import pprint
from urllib import parse

import lassie
import requests
from parsel import Selector

from data.app_data import htaccess


class Rest:
    def __init__(self):
        self.requests = requests.Session()



    def get_data(self,*ars):
        data = self.requests.get(*ars)
        return data
    def crawl(self,dev):
        t_link=[]
        response = requests.get(dev)
        links = re.findall('(?:href=")(.*?)"', response.text)
        for l in links:
            l = parse.urljoin(dev,l)
            if dev in l and l not in t_link:
                t_link.append(l)
            try :
              self.crawl(l)
            except:
                print("Wrong Url href "+l)

    def parsel(self,text):
         selector =  Selector(text=text)
         return selector

    def get_all_pages_Info_over_Website(self, url, links):
        pages = []

        for l in links:
            if l.startswith('http'):
                pages.append(l)
            elif l.startswith('/'):
                pages.append('https://' + url + l)


        for page in pages:
            if page == []:
                pages.remove(page)
        return pages

    def convert_dev_url(self, page):
             return page.replace("https://", htaccess, 1)

    def get_Lassie_object(self,page):
            return (lassie.fetch(page,all_images=True))

    def find_(self,in_, item):
        return self.parsel(in_).css(item)
