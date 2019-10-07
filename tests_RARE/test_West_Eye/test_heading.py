import pytest
import requests
from bs4 import BeautifulSoup

heads =[
'https://westbocaeyecenter.com/view-our-office/',
'https://westbocaeyecenter.com/services/cataract-surgery/acrysof-restor-iol/',
'https://westbocaeyecenter.com/services/cataract-surgery/cataract-yag-laser/',
'https://westbocaeyecenter.com/services/cataract-surgery/tecnis-symfony-symfony-toric-iol/',
'https://westbocaeyecenter.com/services/dry-eyes-allergies/allergic-conjunctivitis/',
'https://westbocaeyecenter.com/services/dry-eyes-allergies/blepharitis/',
'https://westbocaeyecenter.com/services/dry-eyes-allergies/chalazion/',
'https://westbocaeyecenter.com/services/dry-eyes-allergies/corneal-abrasion/',
'https://westbocaeyecenter.com/services/dry-eyes-allergies/excessive-tearing/',
'https://westbocaeyecenter.com/services/dry-eyes-allergies/giant-papillary-conjunctivitis/',
'https://westbocaeyecenter.com/services/dry-eyes-allergies/viral-or-bacterial-conjunctivitis/',
'https://westbocaeyecenter.com/services/laser-vision-correction/lasik-laser-in-situ-keratomileusis/',
'https://westbocaeyecenter.com/services/laser-vision-correction/photorefractive-keratectomy-prk/',
'https://westbocaeyecenter.com/services/routine-eye-care/amblyopia/',
'https://westbocaeyecenter.com/services/routine-eye-care/bifocal-contact-lenses/',
'https://westbocaeyecenter.com/services/routine-eye-care/color-blindness/',
'https://westbocaeyecenter.com/services/routine-eye-care/eye-exam/',
'https://westbocaeyecenter.com/services/routine-eye-care/eyeglasses/',
'https://westbocaeyecenter.com/services/routine-eye-care/eyelid-twitch/',
'https://westbocaeyecenter.com/services/routine-eye-care/eyestrain/',
'https://westbocaeyecenter.com/services/routine-eye-care/low-vision/',
'https://westbocaeyecenter.com/services/routine-eye-care/ocular-migraine/',
'https://westbocaeyecenter.com/services/systemic-eye-diseases/herpes-zoster-shingles-eye-infections/'
]
@pytest.mark.parametrize('h1',heads)
def test_head(h1):
    page = requests.get(h1)
    soup = BeautifulSoup(page.content)
    heading = soup.find_all('h1')
    for h in heading:
        print(h1 , h)
