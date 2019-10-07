import time
from pprint import pprint

url = "http://52.35.36.109/"
def test_hamburger_menu(app):
    app.open(url)
    app.driver.find_element_by_css_selector('nav .buttons .slide-out-widget-area-toggle a').click()
    time.sleep(3)
    menu = app.driver.find_elements_by_css_selector('.menuopen li a')
    pages = [{'link':m.get_attribute('href'),'name':m.text} for m in menu]
    app.driver.find_element_by_css_selector('.buttons .open>span').click()
    pprint(pages)
    for page in pages:
        app.open(page['link'])
        print('Used ' + page['name'],'Opened '+ app.current())

def test_dev_NEWS(app):
    app.open(url)
    app.wbec.toggle_menu()
    app.wbec.wbec_menu()[4].click()
    news = app.driver.find_element_by_css_selector('.post-area')
    posts = news.find_elements_by_css_selector('.post')
    for post in posts:
        app.scroll(post)
        category = post.find_element_by_css_selector('.meta-category a')
        header = post.find_element_by_css_selector('.post-header h3>a')
        date = post.find_element_by_css_selector('.grav-wrap .text span')
        pprint({'category':category.text,'cat_link':category.get_attribute('href'),'title':header.text,'title_link':header.get_attribute('href'),'date':date.text})

def test_dev_WCU(app):
        app.open(url + '/why-choose-us/')
        slider = app.driver.find_element_by_css_selector('.flickity-slider')
        blocks = slider.find_elements_by_css_selector('.inner')
        for block in blocks:
            app.scroll(block)
            print({'name': block.find_element_by_css_selector('span.testimonial-name').text,
                   'title': block.find_element_by_css_selector('span.title').text})
        core =app.driver.find_elements_by_css_selector('.wpb_tabs_nav.ui-tabs-nav li a')
        for c in core:
           print(c.text)
           if  c.get_attribute('class')!='active-tab':
               c.click()
               time.sleep(1)

def test_WCU_blue_buttons(app):
        buttons = []
        bb = app.driver.find_elements_by_css_selector('.blue-btn')
        for b in bb:
            app.scroll(b)
            button = {'name': b.text, 'link': b.get_attribute('href')}
            buttons.append(button)
        for button in buttons:
            app.open(button['link'])
            print(button, 'opened :' + app.driver.title, 'url of opened page : ' + app.driver.current_url)
def test_Reviews(app):
    app.open(url + '/reviews/')
#