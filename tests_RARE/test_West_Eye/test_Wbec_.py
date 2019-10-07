from pprint import pprint

url = "http://wbec.smashedmedia.guru"
def test_dev_services(app):
    app.open(url)
    app.driver.find_element_by_css_selector(".slide-out-widget-area-toggle li>a>span").click()
    blue_menu = app.driver.find_elements_by_css_selector('.menuwrapper')
    navs =blue_menu.find_elements_by_css_selector('li a')
    items_nav = [(app.scroll(s),{'name':s.text,'link':s.get_attribute('href')})for s in navs]
    pprint(items_nav)

