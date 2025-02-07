# // random text --- > no suggestion found ---- 
# // element select ----- list of elements ---- value update 
# // value selected ---- url difference

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.save_screenshot()
driver.get('https://webdriveruniversity.com/Autocomplete-TextField/autocomplete-textfield.html?food-item')
driver.find_element(By.ID,'myInput').send_keys('a')
time.sleep(2)
eElements = driver.find_elements(By.CSS_SELECTOR,"#myInputautocomplete-list > div")
for x in eElements:
    if x.text == "Almond":
        x.click()
        break
driver.find_element(By.ID,'submit-button').click()
if "Almond" in driver.current_url:
    print("testcase pass")
else:
    print('test case fail')


