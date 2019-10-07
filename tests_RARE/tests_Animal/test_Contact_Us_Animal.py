import pytest

from data.app_data import Fake

url='https://philsanimalrentals.com/'
@pytest.mark.skip
def test_app(app):
    app.open(url)
    app.animal.feel_Contact_form( name='test_smashed'+Fake.name, email=Fake.email, phone=Fake.phone, company=Fake.company, message=Fake.message)
    app.animal.send_Feedback()
@pytest.mark.skip
def test_contact_us_page(app):
    app.open(url+'contact-us/')
    app.animal.Contact_form_On_Contact_Us(name=Fake.name, email=Fake.email, phone=Fake.phone, company=Fake.company,message=Fake.message)
    app.animal.send_Feedback()
@pytest.mark.skip
def test_newsletter(app):
     app.open(url)
     app.driver.find_element_by_css_selector('.email input').send_keys(Fake.email)
     app.driver.find_element_by_xpath(".//*[@id='wpcf7-f13063-o2']/form/div[2]/input").click()


