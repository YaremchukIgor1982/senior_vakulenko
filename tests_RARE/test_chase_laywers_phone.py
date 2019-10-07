from assertpy import assert_that


def test_cl(app):
    app.open('https://entertainmentlawyermiami.com')
    menu = app.driver.find_elements_by_css_selector(".menu-item a")
    all = []
    for m in menu:
        app.scroll(m)
        all.append( m.get_attribute('href'))
    for a in all:
        app.open(a)
        phone = app.driver.find_elements_by_css_selector('.side-header-content-2 .fusion-contact-info li a')
        assert_that(phone[0].text).is_equal_to("(305) 373-7665")
        print({"url":a,"page":app.driver.title,"phone":phone[0].text})