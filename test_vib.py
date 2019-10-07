import time
from random import randrange

import pytest

from data.app_data import htaccess
urls={
    '/product/cbd-pain-relief-cream-500mg-2oz/',
    '/product/cbd-pen-tincture-and-topical-bundle/'
}
dev = 'vib.smashedmedia.guru'
@pytest.mark.parametrize('uri',urls)
def test_bundles(app,uri):
    app.open(htaccess+dev+uri)
    time.sleep(2)
    name = randrange(1,100)
    try:
      app.driver.find_element_by_css_selector('.hustle-modal-close svg').click()
    except:
        print("No pop up ")
    app.fullpage_screenshot('{}.png'.format(name),scroll_delay=3)