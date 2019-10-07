from pprint import pprint

from data.data_rare.spec import dev_url

slides_info =[]
def test_navigation_resources(app):
    app.driver.get(dev_url)
    app.spec.go_menu_to('Resources')
def test_cad_gallery(app):
    cad = app.driver.find_element_by_css_selector('.cad-swiper-section')
    cad_slides = cad.find_elements_by_css_selector('.swiper-slide.item')
    slides_info = [(app.scroll(slide),{'title':slide.find_element_by_css_selector('h4').text,
                       'img':slide.find_element_by_css_selector('img').get_attribute('src'),
                       'link': slide.find_element_by_css_selector('a').get_attribute('href')}) for slide in cad_slides]
    pprint(slides_info)

    for slide_link in slides_info:
        app.open(slide_link[1]['link'])
def test_pdf_library(app):
    app.driver.get(dev_url+'/en/resources')
    pdf = app.driver.find_element_by_css_selector('.pdf-swiper-block')
    pdf_slides = pdf.find_elements_by_css_selector('.swiper-slide.item')
    pdf_slides_info = [(app.scroll(slide), {'title': slide.find_element_by_css_selector('h4').text,
                                        'img': slide.find_element_by_css_selector('img').get_attribute('src'),
                                        'link': slide.find_element_by_css_selector('a').get_attribute('href')}) for
                   slide in pdf_slides]
    for slide_link in pdf_slides_info:
        app.open(slide_link[1]['link'])