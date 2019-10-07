import os
import random
import time
from pprint import pprint

import requests
from assertpy import assert_that
from selenium.webdriver.support.select import Select





dir = 'C:\\Users\\Administrator\\PycharmProjects\\Scum\\data\\smashed\\'

class SmashedMedia:


    def __init__(self, app):
        self.app = app

    ########################################Compare
    def change_dir(self):
        full = os.path.realpath(os.path.dirname(os.path.abspath(__file__)) + '\\..\\data\\smashed\\')
        return full

    def get_original_data(self,file):
        full =self.change_dir()
        f = open(full+file, 'r')
        message = f.read()
        f.close()
        return message


#####################################################################################
    def get_Case_Study_thumbnail_info(self, case):
        self.app.scroll(case)
        case_study = {'img':None,'outer_link':None,'title':None}
        case_study['main_img']=case.find_element_by_css_selector('picture>img').get_attribute('src')
        # case_study['img'] = case.find_element_by_css_selector('.links .full-image').get_attribute('href')
        case_study['outer_link'] = case.find_element_by_css_selector('.inner-link').get_attribute('href')
        case_study['title'] = case.find_element_by_css_selector('.links .title').text
        return(case_study)

    def get_Inner_Service_Page_data(self):
        inner_service = {'c_url': None, 'top_header_title':None,'under_title':None,'quote': None }
        inner_service['c_url'] = self.app.driver.current_url
        inner_service['top_header_title']=self.app.driver.find_element_by_css_selector('.sc-main-title h1').text
        inner_service['under_title']=self.app.driver.find_element_by_css_selector('.under-title').text
        cite = self.app.driver.find_element_by_css_selector('.gem-quote>blockquote')
        self.app.scroll(cite)
        inner_service['quote']=cite.text
        inner_service['text_align:']=self.css_of_paragraph()
        return(inner_service)

    def css_of_paragraph(self):
        parag = self.app.driver.find_elements_by_css_selector('p')
        styles = []
        for p in parag:
            self.app.scroll(p)
            st = p.value_of_css_property('text-align')
            styles.append(st)
        return styles


    def all_Inner_services_from_Our_Services_grid(self):
        inner_services = self.app.driver.find_elements_by_css_selector('.services_block a')
        return inner_services

    def get_Inner_service_DATA_from_Our_Services_grid(self, s):
        self.app.scroll(s)
        service_grid = {'title':None,'image':None,'link':None}
        service_grid['link'] = s.get_attribute('href')
        service_grid['image']=s.find_element_by_css_selector('.services_block a .icon-wrapper').get_attribute('style')
        service_grid['title']=s.find_element_by_css_selector('span.service-title').text
        return (service_grid)

    def socials(self):
        socials = self.app.driver.find_elements_by_css_selector('.socials-item')
        soc = []
        for s in socials:
            self.app.scroll(s)
            title = s.get_attribute('title')
            href = s.get_attribute('href')
            st = requests.get(href)
            social = {'title': title, "link": href, 'link_status': str(st.status_code == 200)}
            soc.append(social)
        return soc
    def sitemap_check_notes(self, point):
        pages = self.app.driver.find_elements_by_css_selector(point)
        return[(self.app.scroll(p),{'name':p.text,'page':p.get_attribute('href')})for p in pages]


    def surf_testing_across_links(self,page_links):
        for i in page_links:
            self.app.open(i)
            time.sleep(3)
            print('Opened : ' + self.app.driver.title, "\n"'Used : ' + i);print(self.app.smashed.page_common_layout_info())

    def page_common_layout_info(self):
         logo_displayed = self.app.driver.find_element_by_css_selector('.site-logo').is_displayed()
         print('Logo is presented: ',logo_displayed)
         menu = self.app.driver.find_element_by_css_selector('#primary-menu')
         subs = menu.find_elements_by_css_selector('li>a')
         print(len(subs))
         menu_titles = []
         for s in subs:
             self.app.scroll(s)
             menu_titles.append(s.text)
         foot = self.app.driver.find_element_by_css_selector('.fullwidth-block-inner')
         self.app.scroll(foot)
         social = self.socials()

         layout = {'footer':foot.text,'socials':social,'main_menu':menu_titles}
         pprint(layout)

    def get_Articles_from_Blog(self, a):
        post = {'image': None, 'title': None, 'title_link': None, 'content_cut': None,'date':None}
        post['image']=a.find_element_by_css_selector('.post-image img').get_attribute('src')
        post['title'] = a.find_element_by_css_selector('.post-text-wrap .post-title h3 a').text
        post['title_link'] = a.find_element_by_css_selector('.post-text-wrap .post-title h3 a').get_attribute('href')
        post['content_cut'] = a.find_element_by_css_selector('.post-content p').text
        post['text_align'] = []


        return (post)
    def contact_form(self,name,last_name,phone,email,message):
        form =self.app.driver.find_element_by_css_selector('.wpcf7-form')
        self.app.scroll(form)
        f_name = form.find_element_by_css_selector('.firstname input')
        l_name = form.find_element_by_css_selector('.lastname input')
        phon = form.find_element_by_css_selector('.phone input')
        eml = form.find_element_by_css_selector('.email input')
        text = form.find_element_by_css_selector('.message textarea')
        form.find_element_by_css_selector('.wpcf7-select').click()
        time.sleep(3)
        all = form.find_elements_by_css_selector('option')
        random.choice(all).click()

        f_name.send_keys(name)
        l_name.send_keys(last_name)
        phon.send_keys(phone)
        eml.send_keys(email)
        text.send_keys(message)

        print("Used data for Feedback :");
        pprint({'name': name,'last_name':last_name ,'email': email, 'phone': phone, 'msg': message})

    def contact_form_Home(self, name, website, email):
        form = self.app.driver.find_element_by_css_selector('.wpcf7-form')
        self.app.scroll(form)
        f_name = form.find_element_by_css_selector('.name input')
        phon = form.find_element_by_css_selector('.website input')
        eml = form.find_element_by_css_selector('.email input')
        text = form.find_element_by_css_selector('.Message textarea')

        f_name.send_keys(name)
        text.send_keys('Test. Check contact form on Home Page')
        phon.send_keys('test'+website)
        eml.send_keys('test'+email)

        print("Used data for Feedback :");
        pprint({'name': name, 'website': website, 'email': email })


    def check_Recaptcha(self):
        recapctha = self.app.driver.find_element_by_css_selector('.rc-anchor')
        if recapctha.is_displayed():
            print("Recapctha : " + self.app.driver.find_element_by_css_selector('#recaptcha-anchor-label').text)
        self.app.driver.find_element_by_css_selector('.wpcf7-form-control.wpcf7-submit').click()
        time.sleep(20)

    def get_started_form(self):
        return self.app.driver.find_element_by_css_selector('#cs-download-popup')
    def  fill_data(self,email=None):
        fields = self.get_started_form().find_elements_by_css_selector('input')
        for f in fields:
            name = f.get_attribute('name')
            if name=='your-name':
                f.send_keys('Igor Test SMashedMedia')
            elif name=='your-email':
                f.send_keys(email)
            elif name=='your-phone':
                f.send_keys('+111111111111')
    def  send_form(self):
        return self.get_started_form().find_element_by_css_selector('[type="submit"]')