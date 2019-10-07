from pprint import pprint

from data.data_rare.genet_data import url


def test_start(app):
    app.open(url)
    articles = app.driver.find_elements_by_css_selector('article')
    blog_posts = [app.genetify.get_blog_post_info(article) for article in articles]
    pprint(blog_posts)


