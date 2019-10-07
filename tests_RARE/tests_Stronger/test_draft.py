import time
from pprint import pprint

import pytest

dev = 'https://sc.smashedmedia.guru'

uris = [
    '/for-managers/',
    '/tools-training/',
    "/sales-career/",
    '/past-issues/',
    '/resources/'

]

def test_Home(app):
    app.open(dev)
    post_area = app.driver.find_element_by_css_selector('.post-area')
    posts = post_area.find_elements_by_css_selector('.post-content')
    post_links = []
    for post in posts:
        app.scroll(post)
        post_links.append({"link": post.find_element_by_css_selector('a.entire-meta-link').get_attribute('href'),
                           'title': post.find_element_by_css_selector('h3.title').text})

    pprint(post_links)
    for link in post_links:
        app.open(link['link'])
        time.sleep(2)
        print("used ",link['link'],' ==>>>>',app.driver.current_url)