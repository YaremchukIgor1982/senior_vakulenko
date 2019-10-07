import time

import pytest
from assertpy import assert_that

from data.data_rare.animal_data import old, new


@pytest.mark.parametrize('old_url',old)
def test_migration(app,old_url):
    app.open(old_url)
    time.sleep(4)
    assert_that(new).contains(app.driver.current_url)
    print('Used : '+ old_url,'Redirect :'+app.driver.current_url,"Opened Page Title : "+ app.driver.title)
