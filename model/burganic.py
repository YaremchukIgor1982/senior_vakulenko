class Burganic:

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
    def button_Online_Order(self):
        return (self.app.driver.find_element_by_css_selector('#menu-item-7115'))

    def menu(self):
        return (self.app.driver.find_elements_by_css_selector('sf-menu li.menu-item'))

    def from_header_menu_go_To(self,arg):
        filter(self.app.driver.find_element_by_css_selector('[text="{}"'.format(arg)).click(),self.menu())