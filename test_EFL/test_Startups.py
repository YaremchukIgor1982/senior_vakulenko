import time
prod = 'https://endlessfrontierlabs.com/'
dev = 'https://efl-stage.smashedmedia.guru'
def test_Startups(app):
    app.open(prod)
    app.efl.menu_go_to('Startups')
    items = app.efl.work_items_grid()
    for i in items:
        app.scroll(i)
        print(i.find_element_by_css_selector('.work-item a').get_attribute('href'))


def test_Startups_open_Pop_up(app):
    app.open(prod + '/startups/')
    items = app.efl.work_items_grid()
    items[1].click()
    for i in range(1, 12):
        app.driver.find_element_by_css_selector('.mfp-arrow.mfp-arrow-right.mfp-prevent-close').click()
        time.sleep(3)
        print(app.driver.find_element_by_css_selector('.mfp-img').get_attribute('src'))