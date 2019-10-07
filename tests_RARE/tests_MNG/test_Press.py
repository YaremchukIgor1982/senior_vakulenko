from data.data_rare.mng_data import url

page =[]
def test_press(app):
    app.open(url+'/press')
    menu = app.driver.find_elements_by_css_selector('#mainMenu li a')
    for m in menu:
        app.scroll(m)
        link = m.get_attribute('href')
        print(m.text, link)
        page.append(link)

