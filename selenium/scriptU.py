from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
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

# alert accept 
def accept_alert(driver):
   try:
      WebDriverWait(driver,5).until(EC.alert_is_present())
      driver.switch_to.alert.accept()
   except:
      print("No alert found")

def dismiss_alert(driver):
   try:
      WebDriverWait(driver,5).until(EC.alert_is_present())
      driver.switch_to.alert.dismiss()
   except:
      print("No alert is found")

def take_screenshot(driver, file_name="screenshot.png",save_dir="screenshots"):
   os.makedirs(save_dir,exist_ok=True)
   file_path = os.path.join(save_dir,file_name)
   driver.save_screenshot(file_path)
   print(f"screenshot saved successfully:{file_path}")

def scroll_to_element(driver,locator):
   element = findElement(driver,locator,3,2)
   driver.execute_script("arguments[0].scrollIntoView();",element)


def click_to_element(driver,locator):
   element = findElement(driver,locator,3,2)
   driver.execute_script("arguments[0].click();",element)


def remove_attr(driver,locator):
   element = findElement(driver,locator,3,2)
   driver.execute_script("arguments[0].removeAttr();",element)


def switch_to_new_window(driver):
   lstA = driver.window_handles
   driver.switch_to_window(lstA[-1])


def select_element_dropDown(driver ,locator,index = 0,value= "default",text="default"):
   e = findElement(driver,locator,2,3)
   select = Select(e)
   if(index != 0):
      select.select_by_index(index)
   elif value != "default":
      select.select_by_value(value)
   elif text != "default":
      select.select_by_visible_text(text)











