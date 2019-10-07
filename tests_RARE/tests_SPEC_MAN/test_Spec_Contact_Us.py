from faker import Faker

from data.data_rare.spec import dev_url


def test_empty_form(app):
    app.open(dev_url + '/en/contact-us')
    app.spec.submit_feedback()


def test_contact_us(app):
    last = Faker().last_name()
    email = Faker().email()
    company = Faker().company()
    message = Faker().paragraphs(nb=3, ext_word_list=None)
    app.open(dev_url + '/en/contact-us')
    contact_form = app.spec.contact_form()
    app.spec.input_data(contact_form, last, email, company, message)


def test_submit_form(app):
    app.spec.submit_feedback()
    print(app.spec.alert().text)
