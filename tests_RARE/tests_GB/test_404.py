import time

import pytest

from data.data_rare.gb_data import closed


@pytest.mark.parametrize('url',closed)
def test_404_Ui(app,url):
    app.open(url)
    time.sleep(5)
    print('Url ' +url,app.driver.title)

# @pytest.mark.parametrize('url',closed)
# def test_Back_404(url):
#     check = requests.get(url)
#     print('Url ' + url,'Response Status',check.status_code)
