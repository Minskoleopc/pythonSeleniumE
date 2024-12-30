from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time
driver = webdriver.Chrome()
driver.get('https://webdriveruniversity.com/Actions/index.html')
actions = ActionChains(driver)

# Testcase 1
# Drag and drop 
# draggle = driver.find_element(By.ID,'draggable')
# droppable = driver.find_element(By.ID,'droppable')
# print(droppable.find_element(By.TAG_NAME,'p').text)
# actions.drag_and_drop(draggle,droppable).perform()
# print(droppable.find_element(By.TAG_NAME,'p').text)

# Testcase 2
# hover , click , alert
hoverE = driver.find_element(By.CSS_SELECTOR,'#div-hover > div.dropdown.hover > button')
actions.move_to_element(hoverE).perform()
time.sleep(1)
linkE = driver.find_element(By.CSS_SELECTOR,"#div-hover > div.dropdown.hover > div > a")
linkE.click()
alert = driver.switch_to.alert
alert.accept()







