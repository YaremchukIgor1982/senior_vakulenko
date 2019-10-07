import requests
from bs4 import BeautifulSoup


# def test_parse_Blog():
#     blogposts = []
#     page = requests.get('https://regency.smashedmedia.guru/'+'blog')
#     soup = BeautifulSoup(page.content, 'html.parser')
#     posts = soup.find_all('article',attrs=({'class':'post'}))
#     print(len(posts))
#     for post in posts:
#         link = post.find('a',attrs=({'class':'entire-meta-link'}))
#         image = post.find('span',attrs=({'class':'post-featured-img'})).find('img')
#         date = post.find('div',attrs=({'class':'article-content-wrap'})).find('span')
#         title = post.find('h3').find('a')
#         cut = post.find('div',attrs=({'class':'excerpt'}))
#         blogposts.append({'link':link['href'],'image':image['src'],'publish_date':date.text,
#                'title':title.text,'title_link':title['href'],'content':cut.text})
#     for blogpost in blogposts:
#         inner = requests.get(blogpost['link'])
#         inner_page= BeautifulSoup(inner.content,'html.parser')
#         for href in inner_page.find_all('a'):
#             try:
#              pprint({'page':blogpost['link'],'link_text_name':href.text,'url':href['href']})
#             except:
#               print(href)
from data.app_data import htaccess


def test_blog(app):
    app.open(htaccess + 'regency.smashedmedia.guru/blog')
    app.fullpage_screenshot('Blog.png',scroll_delay=1)