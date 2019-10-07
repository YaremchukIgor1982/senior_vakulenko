import time
from pprint import pprint

from tests_SM.test_SM_Ui import url


def test_sm_services(app):
    app.open(url)
    inner_services = app.smashed.all_Inner_services_from_Our_Services_grid()
    service_pages = [app.smashed.get_Inner_service_DATA_from_Our_Services_grid(s) for s in inner_services]

    links = [service['link'] for service in service_pages]
    pprint(links)
    pages = [(app.open(service_page),app.smashed.get_Inner_Service_Page_data())for service_page in links]

    pprint(pages)










