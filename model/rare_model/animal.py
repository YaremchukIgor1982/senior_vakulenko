from pprint import pprint


class Animal:
    def __init__(self, app):
        self.app = app
        self.driver = app.driver

    def feel_Contact_form(self, name, email, phone, company, message):
        self.driver.find_element_by_css_selector('.full-name input').send_keys('smashed' + name)

        self.driver.find_element_by_css_selector('.your-email input').send_keys(email)

        self.driver.find_element_by_css_selector('.phone-number input').send_keys(phone)

        self.driver.find_element_by_css_selector('.company-name input').send_keys('smashed' + company)

        self.driver.find_element_by_css_selector('.your-message textarea').send_keys('smashed test',message)
        print("Used data for Feedback :");pprint({'name':name,'email':email,'phone':phone,'company':company,'msg':message})

    def send_Feedback(self):
        self.driver.find_element_by_css_selector('p .wpcf7-form-control.wpcf7-submit').click()
        self.app.logger.info('Send Feedback is clicked')

    def Contact_form_On_Contact_Us(self, name, email, phone, company, message):
        self.driver.find_element_by_css_selector('.first-name input').send_keys(name+' Smashed')

        self.driver.find_element_by_css_selector('.last-name input').send_keys('Test')

        self.driver.find_element_by_css_selector('.your-email input').send_keys(email)

        self.driver.find_element_by_css_selector('.your-phone input').send_keys(phone)

        self.driver.find_element_by_css_selector('.your-message textarea').send_keys(message)
        print("Used data for Feedback :");
        pprint({'name': name, 'email': email, 'phone': phone, 'company': company, 'msg': message})

