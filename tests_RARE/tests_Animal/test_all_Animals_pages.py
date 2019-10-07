from pprint import pprint

url ='https://philsanimalrentals.com'
def test_layout_header(app):
    app.open(url+'/sitemap')
    links = app.driver.find_elements_by_css_selector('li.page_item>a')
    pages = [{'name':l.text,'link':l.get_attribute('href')} for l in links]
    pprint(pages)
    for page in pages:
        app.open(page['link'])
        print('used : '+page['link'],'opened : '+app.driver.current_url)