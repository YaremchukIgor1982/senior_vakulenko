import time

from appium import webdriver


def test_appium():
    desired_caps={

        'platformName': 'Android',
        'platformVersion': '9.0',
        'deviceName': '5554',
        'browserName':'Chrome'

    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(3)
    driver.get("https://jiffylubeorlando.com")