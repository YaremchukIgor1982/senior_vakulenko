import pytest

dev = 'http://burganic.smashedmedia.guru/'
uris = [
       '/',
    'about',
    'menu',
    'organic',
    'contact-us',
    'menu-inner',
    'support-local'
]
@pytest.mark.parametrize('uri',uris)
def test_Page_UI(emulator,uri):
        emulator.open(dev+uri)
        if uri=='/':
                uri='home'
        emulator.full_screen(uri)