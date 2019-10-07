from pprint import pprint

from data.data_rare.mng_data import seo_links_redirects_path


def test_ty(app):
    data = app.get_Excel_data(seo_links_redirects_path)
    pprint()