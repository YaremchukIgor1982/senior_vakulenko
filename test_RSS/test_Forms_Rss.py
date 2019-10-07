import time

import pytest

from data.app_data import htaccess
from test_RSS.test_Regency_Api import dev
menus =[
    "Contact",
    "Dealer"
]

@pytest.mark.parametrize("uri",menus)
def test_Forms(app,uri):
    app.open(htaccess +dev)
    menu = app.regency.get_all_menu()
    time.sleep(2)
    filter(app.driver.find_element_by_link_text(uri).click(), menu)
    time.sleep(2)
    getattr(app.regency,"proceed_form_{}".format(uri))()
    app.driver.save_screenshot("{}_form.png".format(uri))
    print(app.contact.response_WPCF_7())
    app.driver.save_screenshot("{}_success_response.png".format(uri))

# def test_Shutter_form(app):
#     app.open(htaccess+"regency.smashedmedia.guru/shutter-buying-checklist/")
#     app.regency.proceed_form_Contact()
#     print(app.contact.response_WPCF_7())
#     app.driver.save_screenshot("{}_shutter_response.png".format(app.driver.title))