import json
import pandas as pd
import time
from pprint import pprint
import glob
from PIL import Image
import pytest

from conftest import ghost
from data.app_data import htaccess
from test_EFL.test_EFL import filters

dev = 'efl-dev.smashedmedia.guru'
prod = 'https://endlessfrontierlabs.com/'
new_mentors = [
    'David Sica',
    'Peter Pfeiffer',
    'Oliver Mitchell',
    'Nasir Memon',
    'Brian Hirsch',
    'Nikhil Gupta',
    'Brenton Fargnoli',
    'Nicole McKnight'
]

# def test_mentors_grid_Mentors_inner_Pages(app,mdb):
#     app.open(dev)
#     app.efl.menu_go_to('Mentors')
#     grid = app.efl.work_items_grid()
#     mentors1 = [app.efl.mentor_info(mentor) for mentor in grid]
#     print(json.dumps(mentors1, indent=4))

    # edb = mdb.db('efl')
    # collection = edb.collection['mentors']
    # collection.insert_many(mentors1)
    # #
    # mentors = ([u for u in collection.find()])
    # pprint(json.loads())
    # df2 = pd.DataFrame(mentors, columns=['name','info'])
    # print(df2)

def test_Mentors_inner_PopUPs(app):
    app.open(htaccess +dev)
    app.efl.menu_go_to('Mentors')
    # footer = app.driver.find_element_by_css_selector('#footer-outer')
    app.fullpage_screenshot('mentors.png',scroll_delay=3)
    grid = app.efl.work_items_grid()
    grid.reverse()
    time.sleep(3)
    for mentor in grid:
        app.scroll(mentor)
        time.sleep(1)
        mentor.click()
        opened = app.efl.mentor_pop_up_info()
        app.driver.get_screenshot_as_file('{}.png'.format(opened['name']))
        print("Catch "+ opened['name'])
        time.sleep(2)
        app.driver.find_element_by_css_selector('.mfp-close').click()
        # with open('{}.png'.format(opened['name']), 'rb') as file:
        #     img = Image.open(file)
        #     img.show()

# def test_new_added_Mentors(ghost):
#         ghost.open(prod)
#         ghost.efl.menu_go_to('Mentors')
#         ghost.fullpage_screenshot('mentors.png', scroll_delay=3)
#         grid = ghost.efl.work_items_grid()
#         grid.reverse()
#         for mentor in grid:
#             ghost.scroll(mentor)
#             men = ghost.efl.mentor_info(mentor)
#             if men['name'] in [new_mentors]:
#                            print(men['name'])
            # if men['name'] in [new_mentors]:
            #      mentor.click()
            #      opened = app.efl.mentor_pop_up_info()
            #      app.driver.get_screenshot_as_file('{}.png'.format(opened['name']))
# def test_opened_images():
#     images = glob.glob("test_EFL/*.png")
#     for image in images:
#         with open(image, 'rb') as file:
#             img = Image.open(file)
#             img.show()



# @pytest.mark.parametrize('filter', filters)
# def test_filters_mentor_grid(app, filter):
#     app.open(dev + '/mentors/')
#     app.driver.find_element_by_css_selector('[data-filter="{}"]'.format(filter)).click()
#     time.sleep(2)
#     grid = app.efl.work_items_grid()
#     for mentor in grid:
#         time.sleep(1)
#         team = app.efl.mentor_info(mentor)
#         pprint(team)
#     app.driver.find_element_by_link_text('All').click()