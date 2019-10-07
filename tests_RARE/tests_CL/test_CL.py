import time

url = "https://entertainmentlawyermiami.com"
def test_smoke(app):
    app.open(url)
    time.sleep(5)
    # player_status = app.driver.execute_script("return document.getElementById('player').player.isMuted()")
    # print(player_status)
    sidebar = app.driver.find_element_by_css_selector('.side-header-content')
    print(sidebar.text)
    footer = app.driver.find_element_by_css_selector('.fusion-footer .fusion-copyright-notice')
    print(footer.text)