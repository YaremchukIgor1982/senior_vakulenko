from faker import Faker


class RSS:
    def __init__(self,app):
        self.app = app
        self.driver = app.driver
        self.form = app.contact


    def proceed_form_Contact(self):
        name = Faker().first_name()
        last = Faker().last_name()
        phone = Faker().msisdn()
        email = Faker().email()
        sentence = Faker().sentence()
        self.app.contact.to_input('[name="first-name"]').send_keys(name)
        self.app.contact.to_input('[name="last-name"]').send_keys(last)
        self.app.contact.to_input('[name="phone"]').send_keys(phone)
        self.app.contact.to_input('[name="your-email"]').send_keys(email)
        self.app.contact.to_input('[name="your-message"]').send_keys(sentence)
        self.app.contact.button_Submit().click()
        return {"name":name,"last":last,"phone":phone,"email":email,"sentence":sentence}


    def proceed_form_Dealer(self):
        name = Faker().first_name()
        company = Faker().company()
        phone = Faker().msisdn()
        email = Faker().email()
        self.app.driver.switch_to_frame(self.app.driver.find_element_by_xpath('//iframe'))
        self.app.contact.to_input('[name="your-name"]').send_keys(name)
        self.app.contact.to_input('[name="company-name"]').send_keys(company)
        self.app.contact.to_input('[name="phone"]').send_keys(phone)
        self.app.contact.to_input('[name="your-email"]').send_keys(email)
        self.app.contact.button_Submit().click()
        self.app.driver.switch_to_default_content()

    def button_Submit(self, page):
        uri=""
        frame = self. app.driver.find_element_by_xpath("//iframe")
        if uri == page:
            self.app.driver.switch_to.frame(frame)
            self.app.contact.button_Submit().click()
            self.app.driver.switch_to.default_content()
        else:
            self.app.contact.button_Submit().click()

    def header(self):
        return self.driver.find_element_by_css_selector("#top")
    def footer(self):
        return self.driver.find_element_by_css_selector("#footer-outer")
    def logo(self):
        logo = self.header().find_element_by_css_selector("#logo")
        image = logo.find_element_by_css_selector("img").get_attribute("src")
        return ({"logo": logo.get_attribute("href"), "image": image})

    def get_all_menu(self):
        return (self.header().find_elements_by_css_selector("li.menu-item"))

    def menu_item_info(self,t):
            self.app.scroll(t)
            m = t.find_element_by_css_selector("a")
            name = m.text
            link = m.get_attribute('href')
            page=({"id": t.get_attribute("id"), "name": name, "link": link})
            return page

    def footer_info(self):
        logo = self.footer().find_element_by_css_selector(".footer_area_1 #logo_footer")
        logo_image= logo.find_element_by_css_selector("img").get_attribute("src")
        logo = {"link":logo.get_attribute('href'),"image":logo_image}
        adress= self.footer().find_element_by_css_selector(".footer_area_1 #text-5").text
        footer_menu = self.footer().find_elements_by_css_selector(".menu-discover-container li")
        menu = [self.menu_item_info(f) for f in footer_menu]
        footer_cats = self.footer().find_elements_by_css_selector(".menu-categories-container li")
        cats = [self.menu_item_info(f) for f in footer_cats]
        other = self.footer().find_elements_by_css_selector(".footer_area_4 .widget_nav_menu")
        fourth = []
        for o in other:
            chapter = o.find_element_by_css_selector(".widget_nav_menu h4").text
            point = self.menu_item_info(o)
            bla = {"name":chapter,"menu":point}
            fourth.append(bla)
        return({"footer_logo":logo,"address":adress,"footer_menu":menu,"categories":cats,"contatcs":fourth})







