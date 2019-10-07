import time
from pprint import pprint

import pytest

from data.smashed.migrate import console, ends
from data.smashed.sm_data import sitemap, regression

url ='https://smashedmedia.com/'

# @pytest.mark.parametrize('extra',console)
# def test_migration_all_links(app,extra):
#     app.open(extra)
#     time.sleep(5)
#     page={'page':app.driver.title,'USED_link':extra,'redirect_to':app.driver.current_url}
#     pprint(page)
#
#
# @pytest.mark.parametrize('error',regression)
# def test_error(app,error):
#     app.open(url + error)
#     time.sleep(5)
#     page = {'page': app.driver.title, 'old_link':error, 'redirect_to': app.driver.current_url}
#     pprint(page)
#     print(app.smashed.page_common_layout_info())
#
# @pytest.mark.parametrize('end',ends)
# def test_migration_all_links(app,end):
#     app.open(url + end)
#     time.sleep(5)
#     page={'page':app.driver.title,'old_link':end,'redirect_to':app.driver.current_url}
#     pprint(page)

@pytest.mark.parametrize('sitemap_item',sitemap)
def test_sitemap_pages(app,sitemap_item):
    app.open(url+'sitemap/')
    pprint(app.smashed.sitemap_check_notes(sitemap_item))

    # app.smashed.surf_testing_across_links(links)