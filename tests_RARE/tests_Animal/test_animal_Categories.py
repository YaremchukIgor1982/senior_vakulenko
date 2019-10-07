import time
from pprint import pprint

import pytest


url ='https://philsanimalrentals.com'
links=[]
def test_layout_header(app):
    app.open(url)
    animals = app.driver.find_element_by_css_selector('.animal-drd')
    app.scroll(animals)
    l = animals.find_elements_by_css_selector('.mkd-drop-down-start li a')
    page_link = [link.get_attribute('href') for link in l]
    for item in page_link:
        app.open(item)
        if app.driver.find_elements_by_css_selector('.mkd-btn'):
            buttons = app.driver.find_elements_by_css_selector('.mkd-btn')
            for b in buttons:
                app.scroll(b)
                print(app.driver.title, b.get_attribute('target'))
        else:
            print("No buttons Read More Here",app.driver.title)
def test_pages_for_images(app):
    for p in links:
        app.open(p)
        img = app.driver.find_elements_by_css_selector('img')
        images=[]
        for i in img:
            app.scroll(i)
            time.sleep(3)
            src = i.get_attribute('src')
            images.append(src)
        print(p,'Opened : '+app.driver.title)
        pprint(images)