'# -*- coding: utf-8 -*-'
import time

from data.data_rare.mng_data import url


def test_open_morrocana(app):
    app.open(url)
    app.morrocana.check_Page()
def test_home_Treatment_Mask(app):
    features = app.driver.find_elements_by_css_selector('.feature-box.hidden-xs')
    for c in features:
        time.sleep(2)
        clp = c.find_element_by_css_selector('.box-content>span').text
        media = c.find_element_by_css_selector('.box-image>img').get_attribute('src')
        print("Feature :"+clp, media)

    # panels = app.driver.find_elements_by_css_selector('.panel-block-row')
    # for p in panels:
    #     app.scroll(p)

    # slider = app.driver.find_element_by_css_selector('.table-container')
    # app.scroll(slider)
    # clicker = slider.find_elements_by_css_selector('.tabs-container>label')
    #
    # for c in clicker:
    #     app.scroll(c)
    #     if c.get_attribute('class')==('active'):
    #         title = slider.find_element_by_css_selector('.title')
    #         print(title.text)
    #         time.sleep(3)
    #     elif c.get_attribute('class') != ('active'):
    #         c.click()






# https://github.com/pytest-dev/pytest-html