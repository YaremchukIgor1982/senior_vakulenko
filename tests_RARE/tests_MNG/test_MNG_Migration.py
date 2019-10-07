# -*- coding: utf-8 -*-
import time

import pytest

from data.data_rare.mng_data import migrate, url


@pytest.mark.parametrize('old_url',migrate)
def test_migration(app,old_url):
    app.open(url + old_url)
    print('Old url : '+ old_url,"Opened :" + app.driver.current_url,'Page title '+app.driver.title)
    time.sleep(3)