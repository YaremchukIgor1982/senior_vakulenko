import time

from data.data_rare.genet_data import url


def test_side_bar(app):
    app.open(url)
    time.sleep(2)
    app.driver.find_element_by_css_selector('.qodef-menu-area .qodef-side-menu-button-opener span').click()
    side_bar = app.driver.find_element_by_css_selector('section')
    title = side_bar.find_element_by_css_selector('p')
    address = side_bar.find_elements_by_css_selector('.qodef-icon-widget-holder')
    print(title.text)
    for a in address:
        hr = a.get_attribute('href')
        blank = a.get_attribute('target')
        content = a.find_element_by_css_selector('span').text
        print('Link '+hr,"Tab "+blank,'Name ' +content)
    socials = side_bar.find_elements_by_css_selector('.qodef-social-icon-widget-holder')
    for s in socials:
        target_social = s.get_attribute('target')
        link = s.get_attribute('href')
        icon = s.find_element_by_css_selector('span').get_attribute('class')
        print('Socials -',"Tab "+ target_social,"Link " + link, 'With Icon '+icon)
