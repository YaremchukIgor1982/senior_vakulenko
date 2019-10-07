from data.app_data import htaccess
dev = "regency.smashedmedia.guru/"




def test_responsive(emulator):
    df = emulator.convert_from_excel('C:\\Users\Administrator\PycharmProjects\Scum\\test_RSS\RegencyShutterMetaData.xlsx')
    xl = []
    for index, value in df.iterrows():
        xl.append({"page": value['Web Page'], 'url': value['Web Page URL']})
    for x in xl:
        u_dev = x['url'].replace('https://regencyshutter.com/', dev, 1)
        emulator.open(htaccess + u_dev)
        emulator.fullpage_screenshot("mobile_{}.png".format(x['page']),scroll_delay=2)

