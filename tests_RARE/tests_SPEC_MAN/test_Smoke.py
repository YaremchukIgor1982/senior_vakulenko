# def test_urls(rest):
#     page = rest.get_data(dev_url)
#     html = json.loads(page.content)
#     mark_up = BeautifulSoup(decodestring(html), 'html.parser')
#     links = mark_up.find_all('a')
#     anchors= []
#     for link in links:
#         href = link.get('href')
#         anchor={'link':link.text,'href':href}
#         anchors.append(anchor)
#     pprint(anchors)
#
# def test_menu(app):
#     app.driver.get(dev_url)
#     menu = app.spec.menu()
#     menu_items = [app.spec.menu_item(item)for item in menu]
#     pprint(menu_items)
# def test_slider_home(app):
#     gallery = app.spec.product_gallery()
#     product_on_home =[app.spec.product_from_home(item)for item in gallery]
#     pprint(product_on_home)
#
#
# def test_footer(app):
#     footer = app.driver.find_element_by_css_selector('.footer')
#
#     attr =footer.find_elements_by_css_selector('li a')
#     for a in attr:
#         print({'name':a.text,'link':a.get_attribute('href')})



#
# def test_navigation_to_product_catalog(app):
#     app.driver.get(dev_url)
#     app.spec.go_menu_to('Products')
#     app.spec.go_menu_to('Product Catalog')
# def test_side_bar_menu(app):
#     left_side = app.driver.find_element_by_css_selector('.left-bar-section .left-bar')
#     bar_menu = left_side.find_elements_by_css_selector('li')
#     menu = [{'title':bar.find_element_by_css_selector('h4').text,
#              'link':bar.find_element_by_css_selector('a').get_attribute('href')}
#             for bar in bar_menu]
#     pprint(menu)
# def test_address_bar(app):
#     address = app.driver.find_element_by_css_selector('.address')
#     pprint({'email':address.find_element_by_css_selector('.email').text,
#             'office':address.find_element_by_css_selector('.office').text,
#             'tollfree':address.find_element_by_css_selector('.tollfree').text,
#             'fax':address.find_element_by_css_selector('.fax').text})
#
# def test_product_gallery(app):
#     app.driver.get(dev_url+'/en/store')
#     store_list = app.driver.find_element_by_css_selector('.store-list')
#     items = store_list.find_elements_by_css_selector('.product-item')
#     products_info =[(app.scroll(item),{'name':item.find_element_by_css_selector('a.product-title').text,
#                                        'link':item.find_element_by_css_selector('a.product-title').get_attribute('href'),
#                                        'content':item.find_element_by_css_selector('table').text}) for item in items]
#     for product in products_info:
#         app.open(product[1]['link'])
#         assert_that(product[1]['link']).is_equal_to(app.driver.current_url)
        # pprint({'name':app.driver.find_element_by_css_selector('.panel-heading h1 span').text,
        #         'sub':app.driver.find_element_by_css_selector('.panel-heading h2').text,
        #         'content':app.driver.find_element_by_css_selector('.panel-heading p').text})








