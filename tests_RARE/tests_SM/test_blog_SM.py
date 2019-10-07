import time
from pprint import pprint

from faker import Faker

url ='https://smashedmedia.com/'
redirects = []
def test_sm(app):
    app.open(url+'/our-blog/')
    articles = app.driver.find_elements_by_css_selector('.post-item')
    posts=[]
    for a in articles:
        app.scroll(a)
        time.sleep(3)
        # text_align = a.find_element_by_css_selector('p').value_of_css_property('text-align')
        # print(text_align)
        post = app.smashed.get_Articles_from_Blog(a)
        redirects.append(post['title_link'])
        posts.append(post['content_cut'])
def test_redirects(app):
    for p in redirects:
        app.open(p)
        time.sleep(3)
        email = Faker().safe_email()
        author = app.driver.find_element_by_css_selector('.post-meta-author').text
        title = app.driver.title
        meta = app.driver.find_element_by_css_selector('.post-meta-left').text
        blog_post = {'title':title,'author':author,'meta':meta}
        app.driver.find_element_by_css_selector('.cs-download-btn a.lp-btn.lp-btn-pink.service-popup').click()

        app.smashed.fill_data(email)
        app.smashed.send_form().click()
        time.sleep(2)
        pprint("Blog_post : {}".format(blog_post))