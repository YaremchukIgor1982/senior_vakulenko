import time

url = 'https://philsanimalrentals.com'
def test_side_bar(app):
    app.open(url)
    time.sleep(2)
    app.driver.find_element_by_css_selector('#mkd_side_area_opener-2').click()
    side_bar = app.driver.find_element_by_css_selector('section')
    sector = side_bar.find_element_by_css_selector('#text-7')
    print(sector.text)
    socials = side_bar.find_elements_by_css_selector('.normal a')
    for s in socials:
        target_social = s.get_attribute('target')
        link = s.get_attribute('href')

        print('Socials -',"Tab "+ target_social,"Link " + link)
