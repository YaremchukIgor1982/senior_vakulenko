from pprint import pprint

url = "http://wbec.smashedmedia.guru"
def test_dev_WCU(app):
    app.open(url+'/news/')
    news = app.driver.find_element_by_css_selector('.post-area')
    posts = news.find_elements_by_css_selector('.post')
    for post in posts:
        app.scroll(post)
        category = post.find_element_by_css_selector('.meta-category a')
        header = post.find_element_by_css_selector('.post-header h3>a')
        date = post.find_element_by_css_selector('.grav-wrap .text span')
        pprint({'category':category.text,'cat_link':category.get_attribute('href'),'title':header.text,'title_link':header.get_attribute('href'),'date':date.text})
# def test_condition_speciality(app):
    
# def test(app):
# #     img = app.driver.find_elements_by_css_selector('img')
# #     for image in img:
# #         app.scroll(image)
# #         print(image.get_attribute('src'))