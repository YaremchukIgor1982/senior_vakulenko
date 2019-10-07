import time
from pprint import pprint

import pytest
from assertpy import assert_that
uris = [
    '/',
    '/faq/',
    '/about/',
    '/tracks/',
    '/contact/',
    '/startups/',
    '/mentors/',
    '/apply-now/',
    '/deep-tech/',
    '/life-sciences/'

]
dev = 'https://efl-dev.smashedmedia.guru'
@pytest.mark.parametrize('uri',uris)
def test_Home(emulator,uri):
    emulator.open(dev+uri)
    time.sleep(3)
    divs = emulator.driver.find_elements_by_css_selector('.wpb_wrapper')
    for d in divs:
        emulator.scroll(d)
        time.sleep(2)


