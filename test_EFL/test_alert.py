import time

dev = 'https://efl-stage.smashedmedia.guru'



# @pytest.mark.repeat(5)

def test_Apply_Now(app):
    app.open(dev)
    app.efl.menu_go_to('Apply Now')
    app.efl.apply_1_step()
    app.driver.find_element_by_css_selector('a.btn-save-form').click()
    app.efl.sign_up()
    time.sleep(5)
    obj = app.driver.switch_to.alert
    obj.accept()

