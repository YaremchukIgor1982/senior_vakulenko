from pprint import pprint

from faker import Faker


class Genetify:
    def __init__(self,app):
        self.app = app
        self.driver = app.driver

    def get_Product_info(self,p):
        self.app.scroll(p)
        image = p.find_element_by_css_selector('img').get_attribute('src')
        link = p.find_element_by_css_selector('a').get_attribute('href')
        title = p.find_element_by_css_selector('h5')
        title_link = title.find_element_by_css_selector('a').get_attribute('href')
        price = p.find_element_by_css_selector('.price')
        product={'title': title.text, 'title_link': title_link, 'image': image, 'price': price.text, 'link': link}
        return product

    def get_Product_Page_Info(self):
        pr_page_title = self.driver.find_element_by_css_selector('.qodef-single-product-title').text
        price_prod = self.driver.find_element_by_css_selector('.price span').text
        sku = self.driver.find_element_by_css_selector('.sku_wrapper').text
        category = self.driver.find_element_by_css_selector('.posted_in>a').text
        taged = self.driver.find_element_by_css_selector('.tagged_as>a').text
        agenda = self.driver.find_element_by_css_selector('.woocommerce-product-details__short-description>p').text
        return({'title': pr_page_title, 'price': price_prod, 'sku': sku, 'category': category, 'taged': taged,
                'agenda': agenda})

    def get_Socials_product(self):
        socials = self.driver.find_elements_by_css_selector('.qodef-social-share-holder li')
        for s in socials:
            link = s.find_element_by_css_selector('a').get_attribute('onclick')
            print('Socials ' + link)
            print(self.driver.title, self.driver.current_url)

    def get_blog_post_info(self,a):
        self.app.scroll(a)
        title = a.find_element_by_css_selector('.entry-title a')
        category = a.find_element_by_css_selector('.qodef-post-info-category>a')
        post_link = title.get_attribute('href')
        image = a.find_element_by_css_selector('img').get_attribute('src')
        author = a.find_element_by_css_selector('.qodef-post-info-author a')
        socials = self.get_Social_Blog(a)
        return ({'post_link': post_link, 'title': title.text, 'author': author.text, 'img': image,
                'category': category.text, 'socials': socials})


    def get_Social_Blog(self,a):
            opener = a.find_element_by_css_selector('.qodef-social-share-dropdown-opener')
            self.app.scroll(opener)
            social = a.find_elements_by_css_selector('.qodef-social-share-dropdown li')
            socials =[l.get_attribute('class')for l in social]
            return socials

    def Contact_form(self,name, email, phone, last_name , message):
            page = self.driver.title
            self.driver.find_element_by_css_selector('.first-name input').send_keys(name)
            self.driver.find_element_by_css_selector('.last-name input').send_keys(name+'last')
            self.driver.find_element_by_css_selector('.email input').send_keys(email)

            self.driver.find_element_by_css_selector('.phone input').send_keys(phone)
            self.driver.find_element_by_css_selector('.message textarea').send_keys(message,page)
            print("Used data for Feedback :");
            pprint({'name': name, 'email': email, 'phone': phone, 'last_name': last_name, 'msg': message})

