import time
from pprint import pprint
import pytest

from data.smashed.mng_links import mng_links


@pytest.mark.parametrize('link',mng_links)
def test_meta(app,link):
    app.driver.get(link)
    time.sleep(2)
    meta = app.get_meta()
    pprint({'webpage_title':app.driver.title,'page_url':link,'meta':meta})


