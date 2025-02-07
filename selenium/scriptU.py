from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()


# 1 Find element with retry
def findElement(driver,locator,retries=3,delay=2):
    for x in range(retries):
        try:
            return driver.find_element(By.CSS_SELECTOR,locator)
        except:
            time.sleep(delay)
    raise Exception(f'Element not found ......')     

findElement(driver,'#login',4,3)

#2
#Wait for element to be clickable
def wait_for_element_to_be_clickable(driver,locator,timeout=10):
   wait =  WebDriverWait(driver,timeout)
   return wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR,locator))

#3
#Wait for element to be visible
def wait_for_element_to_be_visible(driver,locator,timeout =10):
   wait =  WebDriverWait(driver,timeout)
   return wait.until(EC._element_if_visible(By.CSS_SELECTOR,locator))

# 4
#Click element with wait 
def click_element(driver,locator):
   element = wait_for_element_to_be_clickable(driver,locator)
   element.click()

#5 
# Enter the text into field
def enter_text(driver,locator,text):
   element = wait_for_element_to_be_visible(driver,locator)
   element.clear()
   element.send_keys(text)

# Get text from element 
def get_text(driver,locator):
   element = wait_for_element_to_be_visible(driver,locator)
   return element.text

