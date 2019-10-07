from pprint import pprint

import pytest

from data.smashed.sm_data import sitemap

url = 'https://smashedmedia.com/'


@pytest.mark.parametrize('sitemap_item', sitemap)
def test_sitemap_pages(app, sitemap_item):
    app.open(url + 'sitemap/')
    links = app.smashed.sitemap_check_notes(sitemap_item)
    lf = []
    fl = []
    for l in links:
        app.open(l)
        anchors = app.driver.find_elements_by_tag_name('a')
        for h in anchors:
            page_links = {'url': l, 'link_text': h.text, 'font': h.value_of_css_property("font-family")}
            lf.append(page_links)
    #     paragr = app.driver.find_elements_by_tag_name('p')
    #     for pr in paragr:
    #         p = pr.find_element_by_xpath('ancestor::p')
    #         span_links = {'url': l, 'link_text': p.text, 'font': p.value_of_css_property("font-family")}
    #         fl.append(span_links)
    # print(fl)
    all_fonts = {"links": lf}
    print("Page : " + app.driver.title, app.driver.current_url);pprint(all_fonts)

