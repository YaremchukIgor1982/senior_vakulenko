import json
from pprint import pprint

from test_EFL.test_EFL import dev
import pandas as pd

def test_NewMentors():

    data = pd.read_excel('C:\\Users\Administrator\PycharmProjects\Scum\\test_EFL\\NewMentors.xlsx', index_col=0)
    data_dict = data.to_dict('series')

    print(type(data_dict['First']))

    # app.open(dev)
    # app.efl.menu_go_to('Mentors')
    # grid = app.efl.work_items_grid()
    # mentors1 = [app.efl.mentor_info(mentor) for mentor in grid]
    # print(json.dumps(mentors1, indent=4))