from data.data_rare.genet_data import url


def test_navigate_to_shop(app):
    app.open(url+'shop/')
