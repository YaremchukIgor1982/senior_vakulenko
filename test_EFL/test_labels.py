import time

from faker import Faker

dev = 'https://efl-dev.smashedmedia.guru'
# def test_old_form(app):
#     app.open('https://nyu.qualtrics.com/jfe/form/SV_4TPqk4bldQFh8i1')
#     labels = app.driver.find_elements_by_css_selector('label')
#     emails = app.driver.find_elements_by_css_selector('input')
#     emails[0].send_keys(Faker().email())
#     for l in labels:
#         app.scroll(l)
#         print("step 1 " + l.text)
#     app.driver.find_element_by_css_selector('#NextButton').click()
#     time.sleep(3)
#
# def test_2_step(app):
#     labels = app.driver.find_elements_by_css_selector('label')
#     for l in labels:
#         app.scroll(l)
#         print("step 2 " + l.text)
#     app.driver.find_element_by_css_selector('#NextButton').click()
#     time.sleep(3)
# def test_3_step(app):
#     labels = app.driver.find_elements_by_css_selector('label')
#     for l in labels:
#         app.scroll(l)
#         print("step 3 " + l.text)
#     app.driver.find_element_by_css_selector('#NextButton').click()
#     time.sleep(3)
# def test_4th_step(app):
#     labels = app.driver.find_elements_by_css_selector('.Inner BorderColor.ESTB label')
#     for l in labels:
#         app.scroll(l)
#         print("step 4 " + l.text)
#     app.driver.find_element_by_css_selector('#NextButton').click()
#     time.sleep(3)
# def test_5th_step(app):
#     labels = app.driver.find_elements_by_css_selector('label')
#     for l in labels:
#         app.scroll(l)
#         print("step 5 " + l.text)
#     app.driver.find_element_by_css_selector('#NextButton').click()
#     time.sleep(3)
# def test_6th_step(app):
#     labels = app.driver.find_elements_by_css_selector('label')
#     for l in labels:
#         app.scroll(l)
#         print("step 6 " + l.text)
#
#     time.sleep(3)

def test_Apply_Now(app):
    app.open(dev)
    app.efl.menu_go_to('Apply Now')
    app.efl.apply_1_step()
    app.efl.button_Next().click()
    for i in range(9):
        instance = app.driver.find_element_by_css_selector('.fieldset-cf7mls.cf7mls_current_fs')
        labels = instance.find_elements_by_css_selector('label')
        for f in labels:
            print( f.text)
        app.efl.button_Next().click()
