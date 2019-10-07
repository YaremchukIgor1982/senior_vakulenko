import time
from pprint import pprint


class GB:
    def __init__(self,app):
        self.app = app

    def check_GB_logos(self):
        logo = self.app.driver.find_element_by_css_selector('.qodef-light-logo')
        print('Logo is presented :',logo.is_displayed())
        return(logo.get_attribute('src'))


    def check_Top_banner(self):
        top_banner = self.app.driver.find_element_by_css_selector('#slide-39-layer-1').text
        subtitle = self.app.driver.find_element_by_css_selector('.banner-subtitle').text

        return {'main_banner':top_banner,'sub_banner':subtitle}

    def button_Contact_Block(self):
        button = self.app.driver.find_element_by_css_selector('.qodef-btn-text span')
        return button
    def open_Start_Training(self):
        self.app.driver.find_element_by_css_selector('.qodef-btn-text').click()

    def check_Sidebar_left_info(self):
        side_bar = self.app.driver.find_element_by_css_selector('.left-menu')
        time.sleep(3)
        sider = {'image':None,'info':None}
        sider['image']= side_bar.find_element_by_css_selector('.image').get_attribute('src')
        sider['info']=side_bar.text
        self.app.driver.find_element_by_css_selector('.qodef-close-side-menu-holder').click()
        return (sider)

    def get_Footer_info(self):
        icons = self.app.driver.find_elements_by_css_selector('footer .qodef-icon-widget-holder .qodef-icon-text')
        footer = []
        for i in icons:
            self.app.scroll(i)
            footer.append(i.text)
        return (footer)

    def check_Training_Programs(self):
        training_programs = self.app.driver.find_elements_by_css_selector('.qodef-event-list-item-holder')
        tp=[]
        for t in training_programs:
            self.app.scroll(t)
            time.sleep(1)
            program = {'title': None, 'description': None, 'image': None}
            program['title'] = t.find_element_by_css_selector('.qodef-event-list-item-title').text

            program['description'] = t.find_element_by_css_selector('.qodef-event-list-excerpt').text
            program['image'] = t.find_element_by_css_selector('.qodef-event-list-item-image-inner>a').get_attribute('href')
            tp.append(program)
        return tp

    def check_benefits(self):
        benefits = self.app.driver.find_element_by_css_selector('.qodef-tabs')
        points = benefits.find_elements_by_css_selector('.qodef-tabs-nav li')
        b = []
        for p in points:
            self.app.scroll(p)
            benefit = {'point': None, 'dscrpt': None}
            benefit['point'] = p.text

            benefit['dscrpt'] = benefits.find_element_by_css_selector('.qodef-tab-container').text
            p.click()
            time.sleep(2)
            b.append(benefit)
        return b

    def check_Professors(self):
        proffessors = self.app.driver.find_elements_by_css_selector('.qodef-team')
        pr=[]
        for p in proffessors:
            time.sleep(3)
            trener = {'name': None, 'info': None, 'image': None, 'link': None, 'tab': None}
            trener['tab'] = p.find_element_by_css_selector('.qodef-team-position-main-inner').text

            self.app.scroll(p)
            trener['name'] = p.find_element_by_css_selector('.qodef-team-position').text
            trener['link'] = p.find_element_by_css_selector('.qodef-team-name>a').get_attribute('href')
            trener['info'] = p.find_element_by_css_selector('.qodef-team-content-holder').text
            trener['image'] = p.find_element_by_css_selector('.qodef-team-image img').get_attribute('src')
            pr.append(trener)
        return pr
