from pprint import pprint

url ='https://smashedmedia.com/'
def test_case_stud(app):
    app.open(url+'portfolio/')
    case_filters = app.driver.find_elements_by_css_selector('.button')
    for c in case_filters:
        c.click()
        data_category = c.get_attribute('data-category-id')
        value = c.get_attribute('data-sort-value')
        name = c.find_element_by_css_selector('span').text
        category_case = {'title':name,'value':value,'data_category':data_category}
        print(category_case)
    cases = app.driver.find_elements_by_css_selector('.wrap')
    case_links=[]
    for case in cases:
        inner_case = app.smashed.get_Case_Study_thumbnail_info(case)
        case_links.append(inner_case['outer_link'])
    for case in case_links:
        app.open(case)
        case_page ={"page_title":None,'used':case,'current':app.driver.current_url}
        case_page['page_title']=app.driver.title
        paragraph =app.driver.find_elements_by_css_selector('p')
        pprint(case_page)
        for p in paragraph:
            app.scroll(p)

        headings = app.driver.find_elements_by_css_selector('h3')
        for h in headings:
            print(h.text)




