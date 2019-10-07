
import inspect
import json
import random
import time
from datetime import datetime
from pprint import pprint

import requests
from faker import Faker

from fixture.file_manager import FileManager
from model.wpcf7 import ContactForm7


class EFL:

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.form = app.contact


 ################################### Mobile menu
    def hamburger(self):
        return (self.app.driver.find_element_by_css_selector('.slide-out-widget-area-toggle.mobile-icon'))

    def menu_mobile(self, name):
        menu = self.app.driver.find_elements_by_css_selector('li.menu-item a')
        filter(self.app.driver.find_element_by_link_text(name).click(), menu)

    def mobile_submenu(self,sub):
        return (self.app.driver.find_element_by_link_text(sub))


    def menu_go_to(self, name):
        menu = self.app.driver.find_elements_by_css_selector('nav .sf-menu li.menu-item')
        filter(self.app.driver.find_element_by_link_text(name).click(), menu)

    def submenu_Tracks_go_to(self, sub):
        self.app.scroll(self.app.driver.find_element_by_link_text('Tracks'))
        self.app.driver.find_element_by_link_text(sub).click()

    def newsletter_proceed(self, email):
        self.app.driver.find_element_by_css_selector('.newsletter input[name="your-email"]').send_keys(email)
        self.app.driver.find_element_by_css_selector('.newsletter input[type="submit"]').click()

############################################################              CONTACT FORM
    def contact_form(self, name, email, message):
        self.form.field('[name="your-name"]').send_keys('SmashedMedia ' + name)
        self.form.field('[name="your-email"]').send_keys(email)
        self.form.field('[name="your-message"]').send_keys(message)
        name = self.app.func_name()
        self.app.catch_screen('efl', name)





    #################################################################              MENTORS

    def work_items_grid(self):
        return self.app.driver.find_elements_by_css_selector('.element')

    def mentor_info(self, m):

        self.app.scroll(m)
        self.app.catch_screen('efl')
        name = m.find_element_by_css_selector('.work-info h3').text
        return ({'name': name,
                 'info': m.find_element_by_css_selector('.work-info .mentors-meta p').text,
                 'category': m.find_element_by_css_selector('.work-info .mentors-meta .vert-center--category').text,
                 'link_to': m.find_element_by_css_selector('a.nectar-button').get_attribute('href')})

                 # 'response': requests.get(m.find_element_by_css_selector('a').get_attribute('href')).status_code


    def mentor_pop_up_info(self):
        frame = self.app.driver.find_element_by_css_selector(".mfp-iframe")
        self.app.driver.switch_to_frame(frame)
        time.sleep(2)
        bio = self.app.driver.find_element_by_css_selector(".main-content.mentors-container .col>p").text
        cat = self.app.driver.find_element_by_css_selector(".mentor-cat-block").text
        name =  self.app.driver.find_element_by_css_selector('.single-portfolio .mentors-container #sidebar h3').text
        chair = self.app.driver.find_element_by_css_selector('.single-portfolio .mentors-container #sidebar p').text
        self.app.driver.switch_to_default_content()
        return ({"name":name,"category":cat,"chair":chair,"bio":bio})


    ###############################################################################

    def slider_About_us(self):
        return self.app.driver.find_elements_by_css_selector('.cell')

    def team_member_in_Slider(self, c):
        return ({"name": c.find_element_by_css_selector('.wpb_text_column.wpb_content_element.about_pacman h2').text,
                 'place': c.find_element_by_css_selector('.wpb_text_column.wpb_content_element.about_pacman p').text})

    def swipe_slider(self):
        bullet = self.app.driver.find_elements_by_css_selector('.swiper-pagination-bullets span')
        for b in bullet:
            b.click()

    def check_slider_items(self):
        slider = self.app.driver.find_element_by_css_selector('.swiper-wrapper.default_speed')
        slider_item = slider.find_elements_by_css_selector('.swiper-slide a')
        name = self.app.func_name()
        self.app.catch_screen('efl', name)
        return [{'slider_item': s.get_attribute('href')} for s in slider_item]


    ######################################################################3 FAQ
    def table_FAQ(self):
        return (self.app.driver.find_elements_by_css_selector('.instance-1 .toggles'))

    def sub_table_FAQ(self, t):
        return t.find_elements_by_css_selector('h3')

    def click_to_open_and_get_FaqItem_Info_close(self, p, t):
        self.app.scroll(p)
        p.click()
        sub_text = t.find_element_by_css_selector('p')
        time.sleep(1)
        p.click()
        pprint({'name': p.text, 'sub': sub_text.text})
        name = self.app.func_name()
        self.app.catch_screen('efl', name)

    ########################################################################################################################
    # def form_instance(self):
    #     return self.app.driver.find_element_by_css_selector('.wpcf7')


    def apply_1_step(self):

        self.form.field('[type="email"]').send_keys(
            'igory@smashedmedia.com')
        self.form.field('[name="application-company-name"]').send_keys(
            Faker().company())
        self.form.field('[name="application-company-website"]').send_keys(
            Faker().name())
        name = self.app.func_name()
        self.app.catch_screen('efl', name)

    def button_Next(self):
        instns=self.app.driver.find_element_by_css_selector('.cf7mls_current_fs')
        return instns.find_element_by_css_selector('.apply_contact_form .cf7mls_next')



    def apply_2_step(self):
        time.sleep(1)
        self.form.field('[name="application-primary-contacts-name"]').send_keys(Faker().bs())
        self.form.field('[name="application-primary-contacts-title"]').send_keys(Faker().prefix())
        self.form.field('[name="application-primary-contacts-phone"]').send_keys(Faker().msisdn())
        self.form.field('[name="application-primary-contacts-address"]').send_keys(Faker().street_address())
        name = self.app.func_name()
        self.app.catch_screen('efl', name)

    def apply_3_step(self):
        time.sleep(1)

        self.form.field('[name="application-company-describe"]').send_keys(
            Faker().text(max_nb_chars=602, ext_word_list=None) + ' 10 chars')
        self.form.field('[name="application-company-longterm-vision"]').send_keys(
            Faker().text(max_nb_chars=602, ext_word_list=None) + ' 10 chars')
        self.form.field('[name="application-company-describe-scientific-technological-innovation"]').send_keys(
            Faker().text(max_nb_chars=602, ext_word_list=None) + ' 10 chars')
        name = self.app.func_name()
        self.app.catch_screen('efl', name)

    def apply_4_step(self):
        time.sleep(2)
        self.form.field('[name="application-company-validation"]').send_keys(Faker().bs())
        self.form.field('[name="application-company-plan-protection-technology"]').send_keys('Test Test', Faker().text(max_nb_chars=350, ext_word_list=None))
        self.form.field('[name="application-technology-better-than-alternative"]').send_keys('Test Test', Faker().text(max_nb_chars=350, ext_word_list=None))

        self.form.field('[name="application-company-three-patents-related"]').send_keys('Test Test', Faker().catch_phrase())

        self.form.field('[name="application-company-three-publications-related"]').send_keys('Test Test', Faker().catch_phrase())
        name = self.app.func_name()
        self.driver.get_screenshot_as_file('../screenshots/{}/{}.png'.format('efl', name))

    def apply_5_step(self):
        time.sleep(2)
        self.form.field('[name="application-who-owns-technology"]').send_keys('Test Test', Faker().text(max_nb_chars=350, ext_word_list=None))
        self.form.field('[name="application-hurdles-foresee"]').send_keys('Test Test', Faker().text(max_nb_chars=350, ext_word_list=None))
        self.form.field('[name="application-describe-product"]').send_keys(Faker().text(max_nb_chars=602, ext_word_list=None) + ' 10 chars')
        self.form.field('[name="application-demo-video-url"]').send_keys(Faker().uri())
        self.form.field('[name="application-market-does-product-address"]').send_keys('Test Test', Faker().text(max_nb_chars=350, ext_word_list=None))

    def apply_6_step(self):
        time.sleep(1)
        # checks = self.app.driver.find_elements_by_css_selector('[name="application-company-deep-life-sciences[]"]')
        # random.choice(checks).click()

        self.form.field('[name="application-far-along-product"]').send_keys(
            Faker().text(max_nb_chars=350, ext_word_list=None))
        self.form.field('[name="application-how-long-working-product"]').send_keys(
            Faker().text(max_nb_chars=350, ext_word_list=None))
        self.form.field('[name="application-customers-for-product"]').send_keys(
            Faker().text(max_nb_chars=350, ext_word_list=None))
        name = self.app.func_name()
        self.driver.get_screenshot_as_file('../screenshots/{}/{}.png'.format('efl', name))

    def apply_7_step(self):
        time.sleep(1)
        self.form.field('[name="application-revenues-question"]').send_keys(
            Faker().paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None))
        self.form.field('[name="application-current-competitors"]').send_keys(
            Faker().paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None))
        self.form.field(
            '[name="application-technology-application-related"]').send_keys(
            Faker().text(max_nb_chars=602, ext_word_list=None) + ' 10 chars')
        self.form.field('[name="application-pursued-applications-with"]').send_keys(
            Faker().text(max_nb_chars=350, ext_word_list=None))
        name = self.app.func_name()
        self.driver.get_screenshot_as_file('../screenshots/{}/{}.png'.format('efl', name))

    def apply_8_step(self):
        time.sleep(1)
        self.founders_block()
        self.form.field('[name="application-why-team-best"]').send_keys(
            Faker().text(max_nb_chars=350, ext_word_list=None))
        self.form.field('[name="application-plans-hire-team"]').send_keys(
            Faker().text(max_nb_chars=350, ext_word_list=None))
        name = self.app.func_name()
        self.driver.get_screenshot_as_file('../screenshots/{}/{}.png'.format('efl', name))

    def founders_block(self):
        block = self.form.field('.founders-block .container-fluid')
        fields_row = block.find_elements_by_css_selector('.field-founders')
        for field in fields_row:
            inputs = field.find_elements_by_css_selector('input')
            for i in inputs:
                self.app.scroll(i)
                name = i.get_attribute('name')
                if name.startswith('founder-name-'):
                    i.send_keys(Faker().first_name())
                elif name.startswith('founder-titlerole-'):
                    i.send_keys(Faker().prefix())
                elif name.startswith('founder-linkedin-'):
                    i.send_keys(Faker().uri())
                elif name.startswith('founder-education-'):
                    i.send_keys(Faker().job())
                elif name.startswith('founder-fullparttime-'):
                    i.send_keys("HGHJGKJ")
                elif name.startswith('founder-email-'):
                    i.send_keys(Faker().email())

    def apply_9_step(self):
        time.sleep(1)
        self.form.field('[name="application-incorporated-legal-entity"]').send_keys(
            Faker().text(max_nb_chars=350, ext_word_list=None))
        self.form.field('[name="application-relevant-info-about-company"]').send_keys(
            Faker().text(max_nb_chars=350, ext_word_list=None))
        self.form.field(
            '[name="application-currently-finance-operations"]').send_keys(
            Faker().text(max_nb_chars=350, ext_word_list=None))
        self.form.field('[name="application-taken-investment"]').send_keys(
            Faker().text(max_nb_chars=350, ext_word_list=None))
        self.form.field('[name="application-plan-fund-raising"]').send_keys(
            Faker().text(max_nb_chars=350, ext_word_list=None))
        name = self.app.func_name()
        self.driver.get_screenshot_as_file('../screenshots/{}/{}.png'.format('efl', name))

    def apply_10_step(self):
        time.sleep(2)
        self.form.field('[name="application-about-technology-product"]').send_keys(
            Faker().catch_phrase())
        self.form.field('[name="application-affiliated-another-startup"]').send_keys(
            Faker().text(max_nb_chars=350, ext_word_list=None))
        self.form.field('[name="application-how-hear-efl"]').send_keys(
            Faker().text(max_nb_chars=350, ext_word_list=None))
        name = self.app.func_name()
        self.driver.get_screenshot_as_file('../screenshots/{}/{}.png'.format('efl', name))


    def sign_up(self):
        user_name = Faker().word()
        first_name = Faker().first_name()
        last_name = Faker().last_name()
        email = Faker().email('mailinator.com')
        self.app.driver.find_element_by_css_selector('#signup-username').send_keys(user_name)
        self.app.driver.find_element_by_css_selector('#signup-first-name').send_keys(first_name)
        self.app.driver.find_element_by_css_selector('#signup-last-name').send_keys(last_name)
        with open('C:\\Users\Administrator\PycharmProjects\Scum\data\\users_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(data.values())
            for d in data.values():
                if email==d:
                    email='{}'.format(random.randrange(1,10))+email
        self.app.driver.find_element_by_css_selector('#signup-email').send_keys(email)
        self.app.driver.find_element_by_css_selector('.fieldset--terms .lrm-nice-checkbox__indicator').click()
        self.app.driver.find_element_by_css_selector(
            '.lrm-signup-section .lrm-form .fieldset--submit button[type="submit"]').click()
        # print(self.app(lambda x: x.driver.find_element_by_css_selector('.lrm-form-message.lrm-form-message--init').text))
        name = self.app.func_name()
        self.driver.get_screenshot_as_file('../screenshots/{}/{}.png'.format('efl', name))
        user =({'user': user_name, 'email': email})
        with FileManager('C:\\Users\Administrator\PycharmProjects\Scum\data\\users_data.json', 'r+') as f:
            data = json.load(f)
            data[user['user']] = user['email']
        with FileManager('C:\\Users\Administrator\PycharmProjects\Scum\data\\users_data.json', 'w') as f:
            json.dump(data, f)

    def login_tab(self):
        return (self.app.driver.find_element_by_css_selector('.lrm-switch-to--login'))


    def logIn(self, user):
        username = user['user']
        password = user['password']
        self.app.driver.find_element_by_css_selector('[name="username"]').send_keys(username)
        self.app.driver.find_element_by_css_selector('[name="password"]').send_keys(password)
        self.app.driver.find_element_by_css_selector(
            '.lrm-signin-section .lrm-form .fieldset--submit button[type="submit"]').click()
        name = self.app.func_name()
        self.driver.get_screenshot_as_file('../screenshots/{}/{}.png'.format('efl',name))

