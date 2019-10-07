from faker import Faker

url = 'https://moroccangoldseries.com/'


# @pytest.mark.parametrize('user',logged)
# def test_open(app,user):
#     app.open(url)
#     app.morrocana.account.icon_login_account().click()
#     app.morrocana.account.feel_login_form(user)
#     app.morrocana.account.proceed_login()
#     app.morrocana.account.logout()





def test_sign_up(app):
    fake = Faker()
    app.open('https://moroccangoldseries.com/')
    app.morrocana.account.open_Sign_Up()
    user = app.morrocana.account.fill_Registration_form(fake)

    f=open('C:\\Users\\Administrator\\PycharmProjects\Scum\\data\\mng_users.py')
    lines = f.readlines()
    lines.append(user['email'])
    f.close()
    f = open('C:\\Users\\Administrator\\PycharmProjects\Scum\\data\\mng_users.py', 'w')
    for item in lines:
        f.write("%s\n" % item)
    f.close()


    print('Email is '+user['email'])
    app.morrocana.account.proceed_Register()
    print(app.driver.title)
    note = app.driver.find_element_by_css_selector('.message-success.success.message')
    print(note.text,note.get_attribute('data-ui-id'))
    app.morrocana.account.logout()





