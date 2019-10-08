import time

from appium import webdriver


def test_appium():
    desired_caps = {
      'platformName': 'Android',
      'platformVersion': '9',
      'browserName': 'Chrome',
      'deviceName': '5MG7N18907001831',
      'chromedriverExecutable': '/usr/local/bin/chromedriver'
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
    time.sleep(3)
    driver.get("https://jiffylubeorlando.com")