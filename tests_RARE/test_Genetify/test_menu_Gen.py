from data.data_rare.genet_data import url


def test_go(app):
    app.open(url)
    blocks = app.driver.find_elements_by_css_selector('.main-advantages .vc_column-inner .qodef-iwt')
    links = []
    for b in blocks:
        app.scroll(b)
        link = b.find_element_by_css_selector('a').get_attribute('href')
        name = b.find_element_by_css_selector('.qodef-iwt-content').text
        title = b.find_element_by_css_selector('.qodef-iwt-text').text
        links.append(link)
        print(name,title,link)
    for l in links:
         app.open(l)
         print('Used '+l , 'Opened '+app.driver.current_url)
