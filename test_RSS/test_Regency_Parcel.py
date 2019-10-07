import time
from pprint import pprint

from data.app_data import htaccess

dev = 'regency.smashedmedia.guru'


# def test_Pages(rest):
#    doc = rest.get_data(htaccess+dev).text
#    links = rest.find_(in_=doc,item='a::attr(href)').getall()
#    pages = rest.get_all_pages_Info_over_Website(dev,links)
#    urls = [rest.convert_dev_url(page) for page in pages]
#    for url in urls:
#       reg_page = rest.get_data(url).text
#       reg_inner_links = rest.find_(in_=reg_page,item='::attr(href)').getall()
#       print('Page : '+url)
#       pprint(reg_inner_links)
# pprint([rest.get_Lassie_object(url)for url in urls])

# def test_Images_on_Page(rest):
#    doc = rest.get_data(htaccess+dev).text
#    images = rest.get_all_(in_=doc,item='img::attr(src)')
#    pprint(images)

def test_all_Butons(rest):
    doc = rest.get_data(htaccess + dev).text
    links = rest.find_(in_=doc, item='a::attr(href)').getall()
    internal = []
    external = []
    for l in links:
        if dev in l and l not in internal:
            internal.append(l)
        else:
            external.append(l)

    for i in internal:
        devs = rest.convert_dev_url(i)
        cross = rest.get_data(devs).text
        btns = rest.find_(in_=cross, item='[class^="nectar-"]').getall()

        buttons=[]
        for b in btns:
            name = rest.find_(in_=b, item='::text').get()
            href = rest.find_(in_=b, item='::attr(href)').get()
            buttons.append({'title':name,'link_in': href})
        print(i)
        pprint(buttons)
    # for i in internal:
    #     app.open(i)
    #     btns = app.driver.find_elements_by_css_selector('.nectar-button')
    #     print("Page Ui : " + app.driver.title)
    #     for b in btns:
    #         app.scroll(b)
    #         pprint({'href': b.get_attribute('href'), 'title': b.text, 'dimensions': b.size})
    #         time.sleep(3)
