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
driver.get('https://ui.vision/demo/webtest/frames/')
time.sleep(2)
#driver.find_element(By.CSS_SELECTOR,"#id1 > div > input[type=text]")

# main page  --------> iframe ------ search the element
# if you want to switch to iframe 
# name - attribute - value
# id - attribute - value
# index - index

driver.switch_to.frame(0)
driver.find_element(By.CSS_SELECTOR,"#id1 > div > input[type=text]").send_keys('hi')
time.sleep(2)

# returning to main content page 
driver.switch_to.default_content()
driver.switch_to.frame(1)
driver.find_element(By.CSS_SELECTOR,"#id2 > div > input[type=text]").send_keys('bye')

# switching to iframe3 and then switching to inside the iframe 
driver.switch_to.default_content()
driver.switch_to.frame(2) # frame-3
driver.find_element(By.CSS_SELECTOR,"#id3 > div > input[type=text]").send_keys("hello again")
driver.switch_to.frame(0) # frame3 --- frame-0
if(driver.find_element(By.ID,'i9').is_displayed()):
    print('testcase pass')

driver.switch_to.default_content()
e = driver.find_elements(By.TAG_NAME,"frame")
print(len(e))