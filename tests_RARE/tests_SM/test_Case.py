import time

import pytest


@pytest.mark.skip
def test_case_study_pdf(app):
    app.open('https://smashedmedia.com/our-work/jiffy-lube/')
    app.driver.find_element_by_css_selector('.cs-download-link-new').click()
    time.sleep(3)
    form = app.driver.find_element_by_css_selector('.wpcf7')
    form.find_element_by_css_selector('.your-name input').send_keys('Test')
    form.find_element_by_css_selector('.your-email input').send_keys('test@test.test')
    form.find_element_by_css_selector('.your-phone input').send_keys('(111)11111111')
    form.find_element_by_css_selector('.wpcf7-submit').click()
    time.sleep(10)

    app.driver.execute_script("document.addEventListener('wpcf7mailsent',function(event)")
    print(app.driver.title, app.driver.current_url)