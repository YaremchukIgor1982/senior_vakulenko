import time
from pprint import pprint

import requests
from assertpy import assert_that
from selenium.webdriver.common.keys import Keys

from data.data_rare.mng_data import pwd


class New():
    def __init__(self, name, last, mail):
        self.name = name
        self.last = last
        self.mail = mail


class Mng:
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.scroll = app.scroll

        self.search = Search(self)
        self.UI = Ui(self)
        self.account = Account(self)



    def check_Page(self):
        logos = self.app.driver.find_elements_by_css_selector('.logo')
        logo = []
        for l in logos:
            image = l.find_element_by_css_selector('img ').get_attribute('src')
            logo.append(image)
        title = self.app.driver.find_element_by_css_selector('.page-header>span').text

        breadcrumbs = self.app.driver.find_elements_by_css_selector('.breadcrumbs li.item')
        breads = [b.text for b in breadcrumbs]
        layout = {'top_head_title': title, 'logo': logo, 'breadcrumbs': breads, "url": self.app.driver.current_url}
        return layout

    def proceed_to_register(self):
        self.app.driver.find_element_by_css_selector('.toogle-login').click()
        self.app.driver.find_element_by_link_text('Register').click()

    def fill_Sign_From(self, name, last, mail):
        self.app.driver.find_element_by_css_selector('#firstname').send_keys(name)
        self.app.driver.find_element_by_css_selector('#lastname').send_keys(last)
        self.app.driver.find_element_by_css_selector('#email_address').send_keys(mail)
        pwd = self.app.driver.find_element_by_css_selector('#password')
        pwd.send_keys('Test123#')
        self.app.driver.find_element_by_css_selector('#password-confirmation').send_keys('Test123#')

    def get_Items(self):
        products = self.app.driver.find_elements_by_css_selector('.item.product.product-item')
        return products

    def Item_in_category(self, r):
        self.scroll(r)
        title = r.find_element_by_css_selector('.product-item-name>a')
        price = r.find_element_by_css_selector('.price-box.price-final_price')
        data_product_id = price.get_attribute('data-product-id')
        product_link = r.find_element_by_css_selector('.product-item-photo').get_attribute('href')

        return {'title': title.text, "price": price.text,'data_product_id':data_product_id,'link':product_link}


    def click_Title_for_Open(self, r):
        title_random = r.find_element_by_css_selector('.product-item-name>a')
        title_random.click()

    def get_Product_Info_from_Page(self):
        title_product = self.app.driver.find_element_by_css_selector('.base')
        price_product = self.app.driver.find_element_by_css_selector('.price-box.price-final_price .price')
        stock = self.app.driver.find_element_by_css_selector('.stock.available>span').text
        self.app.scroll(self.information())
        time.sleep(2)
        more_info = self.more_information()
        time.sleep(2)
        details = self.details()
        single = {'title': title_product.text, 'price': price_product.text,'details':details,'info':more_info,'availible':stock}
        print('Opened page :' + self.driver.title)
        return single

    def details(self):
        self.app.driver.find_element_by_css_selector('.product.data.items #tab-label-attributedescription>a').click()
        dscr = self.app.driver.find_element_by_css_selector('.product-data-items-content .value>p').text
        return  dscr

    def more_information(self):
        self.app.driver.find_element_by_css_selector('.product.data.items #tab-label-additional>a').click()
        time.sleep(3)
        tabs = self.app.driver.find_elements_by_css_selector('tbody tr')
        more_i=[]
        for tab in tabs:
            name = tab.find_element_by_css_selector('th').text
            value = tab.find_element_by_css_selector('td').text
            more = {'tab_name':name,'value':value}
            more_i.append(more)
        return more_i
    def information(self):
        inf = self.app.driver.find_element_by_css_selector('.product-detail-infomation')
        return inf

    # def custom_tab(self):
    #     self.app.driver.find_element_by_css_selector('.product.data.items #tab-label-staticproduct_detail_tab>a').click()
    #     materials = self.app.driver.find_element_by_css_selector('.text-center p').text
    #     return materials

    def button_Add_to_cart(self):
        add_cart = self.app.driver.find_element_by_css_selector('#product-addtocart-button>span')
        return add_cart

    def menu_Shop(self, url):
        shop = self.app.driver.find_element_by_xpath('.//*[@href="{}shop.html/"]'.format(url))
        return shop

    def submenu_Shop(self):
        sub_shop = self.app.driver.find_elements_by_css_selector('.em-line-01')
        return sub_shop


class Ui:
    def __init__(self, Mng):
        self.app = Mng

    def check_menu(self):
        menus = []
        points = self.app.driver.find_elements_by_css_selector('.level0>a')
        for p in points:
            self.app.scroll(p)
            href = p.get_attribute('href')
            menu = {"name": p.text, 'href': href, 'status': str(requests.get(href).status_code == 200)}
            menus.append(menu)
        return (menus)

    def check_empty_cart(self):
        self.app.driver.find_element_by_css_selector('.action.showcart').click()

        cart = self.app.driver.find_element_by_css_selector('#minicart-content-wrapper')
        empty_cart = cart.find_element_by_css_selector('.subtitle.empty>span')
        if empty_cart.is_displayed():
            assert_that(empty_cart.text).is_equal_to('You have no items in your shopping cart.')
            print(empty_cart.text)
        close_cart = cart.find_element_by_css_selector('.action.close-nav-button')
        close_cart.click()

##################################################################Search
class Search():
    def __init__(self, Mng):
        self.app = Mng

    def proceed_Search(self, item):
        self.open_search()
        self.send_Search_Query(item)
        time.sleep(3)
        post_links = []
        if self.dropdown_search():
            for p in self.get_Results_from_dropdown():
                self.result_from_dropdown_info(p)
                self.input().send_keys(Keys.ENTER)

        return (post_links)



    def result_from_dropdown_info(self, p):
        self.app.scroll(p)
        return p.text

    def get_Results_from_dropdown(self):
        dr = self.app.driver.find_elements_by_css_selector('.post-item-link')
        return dr

    def send_Search_Query(self, item):
        self.input().send_keys(item)

    def dropdown_search(self):
        d = self.app.driver.find_element_by_css_selector('#mgs-instant-autocomplete-wrapper')
        return d

    def input(self):
        search_input = self.app.driver.find_element_by_css_selector('#search')
        return search_input

    def open_search(self):
        self.app.driver.find_element_by_css_selector('.action-search').click()
class Account():
    def __init__(self,Mng):
        self.app = Mng

    def logout(self):
        self.app.driver.get('http://nudo.smashedmedia.guru/customer/account/logout')

    def feel_login_form(self,user):
        self.app.driver.find_element_by_css_selector('#email_header').send_keys(user)
        self.app.driver.find_element_by_css_selector('#pass_header').send_keys(pwd)
        self.app.driver.find_element_by_css_selector('.sm-accept-gdpr-login').click()

    def proceed_login(self):
        self.app.driver.find_element_by_css_selector('#send2_header').click()

    def fill_Registration_form(self,fake):
        name = 'test'+fake.name()
        email = fake.email()
        last = 'test' + fake.last_name()

        self.app.driver.find_element_by_css_selector('#firstname').send_keys('test' + name)
        self.app.driver.find_element_by_css_selector('#lastname').send_keys(last)
        self.app.driver.find_element_by_css_selector('#email_address').send_keys(email)
        self.app.driver.find_element_by_css_selector('#password').send_keys(pwd)
        self.app.driver.find_element_by_css_selector('#password-confirmation').send_keys(pwd)
        pprint ({'name':name,'email':email,'last':last})

    def open_Sign_Up(self):
        self.icon_login_account().click()
        self.app.driver.find_element_by_css_selector('.acitve-register').click()

    def icon_login_account(self):
        icon = self.app.driver.find_element_by_css_selector('.toogle-login')
        return icon

    def proceed_Register(self):
        self.app.driver.find_element_by_css_selector('#accept_gdpr').click()
        self.app.driver.find_element_by_css_selector('.action.submit.btn.btn-custom').click()