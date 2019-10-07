from pprint import pprint

from data.data_rare.spec import dev_url


def test_spec(app):
    app.open(dev_url+'/en/our-mission')
def test_headings(app):
    heads = app.driver.find_elements_by_css_selector('h2')
    headings = ((app.scroll(h) [h.text]) for h in heads)
    pprint(headings)
# def test_contact_form(app):
#         last = Faker().last_name()
#         email = Faker().email()
#         company = Faker().company()
#         message = Faker().paragraphs(nb=3, ext_word_list=None)
#         app.open(dev_url + '/en/contact-us')
#         contact_form = app.spec.contact_form()
#         app.spec.input_data(contact_form, last, email, company, message)
#         app.spec.submit_feedback()
#         print(app.spec.alert().text)