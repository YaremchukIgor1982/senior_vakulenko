from pprint import pprint

from faker import Faker


class Wbec:
    def __init__(self, app):
        self.app = app

    def contact_form(self):
        return (self.app.driver.find_element_by_css_selector('.wpcf7-form'))

    def fill_Contact_from(self, email, interest, message):
        contact_form = self.contact_form().find_elements_by_css_selector('input')
        for f in contact_form:
            name = f.get_attribute('name')
            if name == 'your-name':
                f.send_keys('Smashed Media')
            elif name == 'your-email':
                f.send_keys(email)
            elif name == 'tel-207':
                f.send_keys('(111)111-1111')
            elif name == 'interested-in':
                f.send_keys(interest)
        self.contact_form().find_element_by_css_selector('textarea').send_keys(message)
        pprint({'email': email, 'interest': interest})

    def click_to_Send_Form(self):
        self.contact_form().find_element_by_css_selector('input[value="Send"]').click()

    def services_links(self):
        return (self.app.driver.find_elements_by_css_selector('a.sm-service-link'))

    def service_link_info(self, l):
        self.app.scroll(l)
        return [{'title': l.find_element_by_css_selector('.sm-service-title').text,
                                          'href': l.get_attribute('href')} ]
    def service_inner_service_info(self,i):
            inner_services = self.app.driver.find_elements_by_css_selector('.services_posts_shortcode .nectar-recent-post-slide')
            inner_service_info = [(self.app.scroll(i), {'title': i.find_element_by_css_selector('h3 a').text,
                                                        'link': i.find_element_by_css_selector(
                                                            'a.blue-btn').get_attribute(
                                                            'href')})]

            return(inner_service_info)
    def toggle_menu(self):
        self.app.driver.find_element_by_css_selector('nav .buttons .slide-out-widget-area-toggle a').click()
    def wbec_menu(self):
        return(self.app.driver.find_elements_by_css_selector('.menuopen li a'))
