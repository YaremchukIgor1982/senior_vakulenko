import time
from pprint import pprint

url ='https://smashedmedia.com/'




def test_UI_home(app):
    app.open(url)
    app.smashed.page_common_layout_info()


def test_Our_Clients(app):
    our_clients = []
    ballons = app.driver.find_elements_by_css_selector('#balloon_wrapper_2 .balloon-image')
    for b in ballons:
        app.scroll(b)
        our_clients.append(b.get_attribute('data-bg'))
    print('Our Clients Slider Ballons');pprint(our_clients)

def test_Certifications(app):
    our_cert = []
    ballons = app.driver.find_elements_by_css_selector('#balloon_wrapper_1 .balloon-image')
    for b in ballons:
        app.scroll(b)
        our_cert.append(b.get_attribute('data-bg'))
    print('Our Certifications Slider Ballons');pprint(our_cert)

def test_services_Black_blok(app):
    creative_skills_black = app.driver.find_elements_by_css_selector('.creative_skills_black .color-bg')
    skills =[]
    for c in creative_skills_black:
        app.scroll(c)
        title = c.find_element_by_css_selector('h5')
        opys = c.find_element_by_css_selector('p')
        block = {'title':title.text,'description':opys.text}
        skills.append(block)
    print("Block Skills");pprint(skills)

def test_service_grid(app):
    inner_services = app.smashed.all_Inner_services_from_Our_Services_grid()
    print('Before selected ',len(inner_services))
    categories = app.driver.find_elements_by_css_selector('.sm-categories li')
    for c in categories:
        app.scroll(c)
        name = c.find_element_by_css_selector('.service-title')
        time.sleep(1)
        c.click()
        print('Service_category is clicked ' + name.text)
        time.sleep(2)
        highlight=app.driver.find_elements_by_css_selector('.sm-blur')
        print(len(highlight))
        for h in highlight:
            app.scroll(h)
            data_id = h.get_attribute('data-id')

            name = h.find_element_by_css_selector('a span').text
            s_c = {'id':data_id,'title':name}
            print(s_c)
