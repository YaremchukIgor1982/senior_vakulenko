from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

userName = "igoryaremchuk2"
accessKey = "2f4HcvKqq8UsvEkE7z7z"
desired_cap = {
 'device': 'iPhone 8 Plus',
 'os_version': '11'
}
desired_cap['app'] = "bs://444bd0308813ae0dc236f8cd461c02d3afa7901d"

driver = webdriver.Remote("http://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_cap)

text_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Text Button"))
)
text_button.click()

text_input = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Text Input"))
)
text_input.send_keys("hello@browserstack.com" + "\n")

time.sleep(5)

text_output = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Text Output"))
)

if text_output!=None and text_output.text=="hello@browserstack.com":
  print ("Test Passed")
else:
  print ("Test Failed")

driver.quit()