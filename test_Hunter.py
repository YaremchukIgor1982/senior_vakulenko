url=''
dev = "regency.smashedmedia.guru/"
def test_meta(ghost):
    df = ghost.convert_from_excel('C:\\Users\Administrator\PycharmProjects\Scum\\test_RSS\RegencyShutterMetaData.xlsx')
    xl = []
    for index, value in df.iterrows():
        xl.append({"page": value['Web Page'], 'url': value['Web Page URL'], "meta title": value['Meta Title'],
                'meta description': value['Meta Description']})
