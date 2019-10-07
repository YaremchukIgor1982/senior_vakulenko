from data.data_rare.mng_data import url


def test_press(app):
    app.open(url+'/blog')
    posts = app.driver.find_elements_by_css_selector('.blog-post')
    blog_posts = [({'title':post.find_element_by_css_selector('.post-title-link').text,
               'link':post.post.find_element_by_css_selector('.post-title-link').get_attribute('href')}) for post in posts]
    print(blog_posts)

    for b in blog_posts:
        app.open(b['link'])
        print(app.driver.title)