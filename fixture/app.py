import inspect
import random
import re
import sys
from urllib.parse import urlparse

import requests
import xlrd
import time
from PIL import Image
from io import BytesIO

from Screenshot import Screenshot_Clipping
from browsermobproxy import Server

from faker import Faker
from selenium import webdriver
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support import ui

from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

from data.app_data import htaccess
from fixture.bmp import ProxyManager
from fixture.file_manager import FileManager
from model.assur import Assurance
from model.fast_guard import FGS
from model.rare_model.animal import Animal
from model.burganic import Burganic
from model.efl import EFL
from model.rare_model.genetify import Genetify
from model.rare_model.gracie import GB
from model.rare_model.morrocana import Mng
from model.regency import RSS
from model.smashed_media import SmashedMedia
from model.rare_model.specmac import Spec
from model.wbec import Wbec
from model.wpcf7 import ContactForm7
from docx import Document

from screen_recorder_sdk import screen_recorder


class App:
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")


    def __init__(self, chrome_options=chrome_options):
        caps = DesiredCapabilities.CHROME
        caps['loggingPrefs'] = {'performance': 'ALL'}
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options,
                                       desired_capabilities=caps)
        self.wait = ui.WebDriverWait(self.driver, 5000, poll_frequency=1.5)

        self.requests = requests
        self.driver.implicitly_wait(10)
        self.screen = Screenshot_Clipping.Screenshot()
        self.contact = ContactForm7(self)
        self.morrocana = Mng(self)
        self.smashed = SmashedMedia(self)
        self.gracie = GB(self)
        self.genetify = Genetify(self)
        self.animal = Animal(self)
        self.spec = Spec(self)
        self.wbec = Wbec(self)
        self.efl = EFL(self)
        self.burger = Burganic(self)
        self.guard = FGS(self)
        self.regency = RSS(self)
        self.assure = Assurance(self)

    def get_meta(self):
        meta_description = self.driver.find_element_by_css_selector("meta[name='description']").get_attribute('content')
        meta_keywords = self.driver.find_element_by_css_selector("meta[name='keywords']").get_attribute('content')
        return {'meta_description': meta_description, 'meta_keywords': meta_keywords}

    def from_menu_go_to(self, menu, menu_item):
        filter(self.driver.find_element_by_link_text(str(menu_item)).click(), menu)

    def get_Excel_data(self, path):
        workbook = xlrd.open_workbook(path)
        worksheet = workbook.sheet_by_index(0)
        first_row = []  # The row where we stock the name of the column
        for col in range(worksheet.ncols):
            first_row.append(worksheet.cell_value(0, col))
        # transform the workbook to a list of dictionaries
        data = []
        for row in range(1, worksheet.nrows):
            elm = {}
            for col in range(worksheet.ncols):
                elm[first_row[col]] = worksheet.cell_value(row, col)
            data.append(elm)
        return (data)

    def scroll(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def browser_alert(self, action):
        obj = self.driver.switch_to_alert()
        print(obj.text)
        getattr(obj, action)()
        self.driver.switch_to.default_content()

    def open(self, *args):
        self.driver.get(*args)

    def current(self):
        cur = self.driver.current_url
        return cur

    def get_link(self, link):
        self.scroll(link)

    def func_name(self):
        return (inspect.stack()[1][3])

    def catch_screen(self, model):

        self.driver.get_screenshot_as_file('../screenshots/{}/{}.png'.format(model, self.driver.title))

    def destroy(self):

        self.driver.close()

    def fullpage_screenshot(self, file, scroll_delay=0.3):
        device_pixel_ratio = self.driver.execute_script('return window.devicePixelRatio')

        total_height = self.driver.execute_script('return document.body.parentNode.scrollHeight')
        viewport_height = self.driver.execute_script('return window.innerHeight')
        total_width = self.driver.execute_script('return document.body.offsetWidth')
        viewport_width = self.driver.execute_script("return document.body.clientWidth")

        # this implementation assume (viewport_width == total_width)
        assert (viewport_width == total_width)

        # scroll the page, take screenshots and save screenshots to slices
        offset = 0  # height
        slices = {}
        while offset < total_height:
            if offset + viewport_height > total_height:
                offset = total_height - viewport_height

            self.driver.execute_script('window.scrollTo({0}, {1})'.format(0, offset))
            time.sleep(scroll_delay)

            img = Image.open(BytesIO(self.driver.get_screenshot_as_png()))
            slices[offset] = img

            offset = offset + viewport_height

        # combine image slices
        stitched_image = Image.new('RGB', (total_width * device_pixel_ratio, total_height * device_pixel_ratio))
        for offset, image in slices.items():
            stitched_image.paste(image, (0, offset * device_pixel_ratio))
        stitched_image.save(file)

    def full_screen(self, name):
        # noinspection PyTypeChecker
        self.screen.full_Screenshot(self.driver, save_path=r'.', image_name='{}.png'.format(name))

    def get_text_from_doc(self):
        document = Document('C:\\Users\Administrator\PycharmProjects\Scum\data\docs\\fungalkeratitis.docx')
        for para in document.paragraphs:
            return (para.text)

    def header(self):
        return self.driver.find_element_by_css_selector("#top")

    def footer(self):
        return self.driver.find_element_by_css_selector("#footer-outer")

    def get_all_menu(self):
        return (self.header().find_elements_by_css_selector("li.menu-item"))

    def menu_item_info(self, t):
        self.scroll(t)
        m = t.find_element_by_css_selector("a")
        name = m.text
        link = m.get_attribute('href')
        page = ({"id": t.get_attribute("id"), "name": name, "link": link})
        return page

    def convert_from_excel(self, file_path):
        return pd.read_excel(file_path, encoding='utf-16')


class Emulator(App):
    options = App.chrome_options
    options.add_experimental_option("mobileEmulation", {"deviceName": "iPhone X"})

    def __init__(self):
        super(Emulator, self).__init__(chrome_options=self.options)


class Headless(App):
    options = App.chrome_options
    options.add_argument("--headless")

    def __init__(self):
        super(Headless, self).__init__(chrome_options=self.options)


class MobProxy(App):
    def __init__(self):
        proxy = ProxyManager()
        self.server = proxy.start_server()
        self.client = proxy.start_client()
        options = App.chrome_options
        options.add_argument("--proxy-server={}".format(self.client.proxy))
        super(MobProxy, self).__init__(chrome_options=options)

    def stop_server(self):
        self.server.stop()

    def stop_client(self):
        self.client.stop()
