import difflib
from pprint import pprint
import diff_match_patch as dmp_module
import docx
import lxml
import pytest
import requests
from bs4 import BeautifulSoup
import sys
arts = [
    'https://wbec.smashedmedia.guru/anti-vegf-treatment-for-wet-amd/',
    'https://wbec.smashedmedia.guru/branch-retinal-vein-occlusion-brvoq/',
    'https://wbec.smashedmedia.guru/corneal-laceration/',
    'https://wbec.smashedmedia.guru/corneal-transplants/',
    'https://wbec.smashedmedia.guru/fungal-keratitis/',
    'https://wbec.smashedmedia.guru/glaucoma-drainage-implant/'
    ]

# @pytest.mark.parametrize('url',arts)
# def test_Text():
#      page= requests.get('https://wbec.smashedmedia.guru/fungal-keratitis/')
#      parser = BeautifulSoup(page.text, 'lxml')
#      parag = parser.find(class_='post').find_all('span')
#
#      for p in parag:
#          print(p.get_text())


def test_ui_text(ghost):
    ghost.open('https://wbec.smashedmedia.guru/fungal-keratitis/')
    text1 = ghost.driver.find_element_by_css_selector('article').text
    text2 = ghost.get_text_from_doc()



    dmp = dmp_module.diff_match_patch()
    diff = dmp.diff_main(text1, text2)
    # Result: [(-1, "Hell"), (1, "G"), (0, "o"), (1, "odbye"), (0, " World.")]
    dmp.diff_prettyHtml (diff)
    # Result: [(-1, "Hello"), (1, "Goodbye"), (0, " World.")]
    pprint(diff)
    #
    # d = difflib.HtmlDiff()
    # diff = difflib.ndiff(text1_lines, text2_lines)
    # print ('\n'.join(list(diff)))


