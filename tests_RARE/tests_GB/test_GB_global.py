from pprint import pprint

import pytest

from data.data_rare.gb_data import gb_urls


@pytest.mark.parametrize('url',gb_urls)
def test_sm_services(app,url):
    app.open(url)
    logo =app.gracie.check_GB_logos()
    app.gracie.open_Start_Training()
    side_bar=app.gracie.check_Sidebar_left_info()
    footer =app.gracie.get_Footer_info()
    programs=app.gracie.check_Training_Programs()
    benefits=app.gracie.check_benefits()
    profi=app.gracie.check_Professors()

    layout = {'logo':logo, 'side_bar': side_bar, 'footer': footer, 'training_programs': programs, 'benefits':benefits, 'professors': profi}
    print("Page for {}".format(url));pprint(layout)









