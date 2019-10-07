import pytest


from fixture.app import App, Emulator, Headless, MobProxy
from fixture.bmp import ProxyManager
from fixture.crawler import Crawler

from fixture.gmail import Inbox
from fixture.mongo_db import MongoDBConnectionManager
from fixture.rest import Rest


@pytest.fixture(scope="session")
def app(request):
    fixture = App()
    request.addfinalizer(fixture.destroy)
    return fixture

@pytest.fixture(scope="session")
def emulator(request):
    fixture = Emulator()
    request.addfinalizer(fixture.destroy)
    return fixture

@pytest.fixture(scope="session")
def ghost(request):
    fixture = Headless()
    request.addfinalizer(fixture.destroy)
    return fixture

# @pytest.fixture
# def andrd(request):
#     fixture = Android()
#     # request.addfinalizer(fixture.destroy)
#     return fixture

@pytest.fixture(scope="session")
def crawl(request):
    fixture = Crawler()
    # request.addfinalizer(fixture.destroy)
    return fixture

@pytest.fixture(scope="session")
def rest(request):
    fixture = Rest()
    # request.addfinalizer(fixture.destroy)
    return fixture

@pytest.fixture(scope="session")
def mail(request):
    fixture = Inbox()
    # request.addfinalizer(fixture.kill_mail_session)
    return fixture
@pytest.fixture()
def mdb(request):
    fixture = MongoDBConnectionManager()
    request.addfinalizer(fixture.close)
    return fixture
@pytest.fixture(scope="session")
def bmp(request):
    fixture=MobProxy()
    return fixture