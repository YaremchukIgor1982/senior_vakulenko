url = "http://wbec.smashedmedia.guru"
def test_dev_WCU(app):
    app.open(url+'/why-choose-us/')
    slider = app.driver.find_element_by_css_selector('.flickity-slider')
    blocks = slider.find_elements_by_css_selector('.inner')
    for block in blocks:
        app.scroll(block)
        print({'name':block.find_element_by_css_selector('span.testimonial-name').text,'title':block.find_element_by_css_selector('span.title').text})
def test_WCU_blue_buttons(app):
    buttons = []
    bb = app.driver.find_elements_by_css_selector('.blue-btn')
    for b in bb:
        app.scroll(b)
        button={'name':b.text,'link':b.get_attribute('href')}
        buttons.append(button)
    for button in buttons:
        app.open(button['link'])
        print(button,'opened :'+app.driver.title,'url of opened page : '+app.driver.current_url)