url ='https://philsanimalrentals.com'
def test_layout_header(app):
    app.open(url)
    menu_header = app.driver.find_element_by_css_selector('#menu-main-menu')
    pages = menu_header.find_elements_by_css_selector('li')
    for p in pages:
        app.scroll(p)
        print('In menu of - '+p.text)
    spans_scroll = app.driver.find_elements_by_css_selector('span')
    for s in spans_scroll:
        app.scroll(s)
def test_footer_layout(app):
    footer = app.driver.find_element_by_css_selector('.mkd-page-footer')
    info = footer.find_elements_by_css_selector('.mkd-grid-col-3')
    for i in info:
        app.scroll(i)
        title = i.find_element_by_css_selector('h3').text
        print(title)
    socials = footer.find_elements_by_css_selector('.textwidget .circle')
    for s in socials:
        app.scroll(s)
        redirect = s.find_element_by_css_selector('a').get_attribute('href')
        print(redirect)
def test_sidebar(app):
    ham = app.driver.find_element_by_css_selector('.mkd-side-menu-button-opener')
    ham.click()
    content = app.driver.find_element_by_css_selector('.mkd-side-menu.right')
    print(content.text)