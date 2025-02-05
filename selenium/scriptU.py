from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()


# 1 Find element with retry
# def findElement(driver,locator,retries=3,delay=2):
#     for x in range(retries):
#         try:
#             return driver.find_element(By.CSS_SELECTOR,locator)
#         except:
#             time.sleep(delay)
#     raise Exception(f'Element not found ......')     

# findElement(driver,'#login',4,3)

#Wait for element to be clickable
def wait_for_element_to_be_click(driver,locator,timeout =10):
   wait =  WebDriverWait(driver,timeout)
   return wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR,locator))