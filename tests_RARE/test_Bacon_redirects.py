import json
from pprint import pprint

import pytest
import requests
from bs4 import BeautifulSoup

scum = [
'https://baconlending.com/the-reason-we-decided-to-change-locations/ -> https://baconlending.com/',
'https://baconlending.com/a-new-beginning-awaits/ -> https://baconlending.com/',
'https://baconlending.com/porttitor-porttitor-mollis-vitae-placerat-2/ -> https://baconlending.com/',
'https://baconlending.com/video-post/',
'https://baconlending.com/nulla-magna/',
'https://baconlending.com/the-field/',
'https://baconlending.com/magna-fringilla-quis-condimentum/',
'https://baconlending.com/porttitor-porttitor-mollis-vitae-placerat/',
'https://baconlending.com/premium-wordpress-themes-bursting-with-quality/',
'https://baconlending.com/suspendisse-vulputate-diam/',
'https://baconlending.com/facilisis-nulla/',
'https://baconlending.com/donec-porta/',
'https://baconlending.com/aenean-laoreet-tortor/',
'https://baconlending.com/ink-in-water/',
'https://baconlending.com/velit-feugiat-porttito/',
'https://baconlending.com/ownage-in-the-mountains/',
'https://baconlending.com/mauris-pharetra-interdum-lorem-2/',
'https://baconlending.com/be-my-guest/',
'https://baconlending.com/ambrose-redmoon/'
]
# @pytest.mark.parametrize('url',scum)
def test_Redirects_BL():
    page = requests.get('https://hotline.ua/mobile/mobilnye-telefony-i-smartfony/294245/?checkout=1')
    soup = BeautifulSoup(page.content,'html.parser')
    box = soup.find_all('div',attrs={'class':'item-info'})
    for b in box:
        print(b)
    # process= {'used_url':url,'get_redirect':page.history,'opened_page':page.url}
    # pprint(dict(process))