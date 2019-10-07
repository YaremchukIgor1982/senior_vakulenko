import pytest

from data.smashed.sm_data import follow


@pytest.mark.parametrize('rel',follow)
def test_rel(app,rel):
    app.open(rel)
    rel = app.driver.find_elements_by_css_selector('meta')
    for r in rel:
        print(app.driver.title,'Content attribute is : '+r.get_attribute('content'))
