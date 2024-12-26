from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
driver = webdriver.Chrome()
driver.get('https://webdriveruniversity.com/')
driver.maximize_window()
# static wait
time.sleep(10)

# implicit wait 

# syntax of implicit wait  
driver.implicitly_wait(10) # wait for up t0 10 seconds for element to appear
try:
    driver.find_element(By.ID,'contact-us')
except:
    print('element not found')

driver.implicitly_wait(20) 
try:
    driver.find_element(By.ID,'contact-us')
except:
    print('login-portal')

# explicit wait (Dynamic wait)
try:
    wait = WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located(By.ID,'contact-us'))
except:
    print('element not found')


# fluent wait (Dynamic wait)
try:
    fluentWait = WebDriverWait(driver,timeout=10,poll_frequency=2,ignored_exceptions=[TimeoutError])
    fluentWait.until(EC.presence_of_element_located(By.ID,'contact-us'))
except:
    print('element not found')