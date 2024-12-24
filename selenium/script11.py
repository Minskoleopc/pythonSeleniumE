from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import time
driver = webdriver.Chrome()

driver.get('https://webdriveruniversity.com/Popup-Alerts/index.html')

def handle_simple_alert():
    print('javascript alert')
    driver.find_element(By.ID,"button1").click()
    time.sleep(3)
    alert = Alert(driver)
    alert.accept()

def handle_confirm_alert_OK():
    print('javascript  confirm alert - OK')
    driver.find_element(By.ID,"button4").click()
    time.sleep(3)
    alert = Alert(driver)
    print(alert.text)
    alert.accept()
    textAlert = driver.find_element(By.ID,"confirm-alert-text").text
    if textAlert == "You pressed OK!":
        print('test case pass')
    else:
        print('test case fail')

def handle_confirm_alert_Cancel():
    print('javascript  confirm alert - Cancel')
    driver.find_element(By.ID,"button4").click()
    time.sleep(3)
    alert = Alert(driver)
    print(alert.text)
    alert.dismiss()
    textAlert = driver.find_element(By.ID,"confirm-alert-text").text
    if textAlert == "You pressed Cancel!":
        print('test case pass')
    else:
        print('test case fail')


def handle_modal_popup():
    pass

  
  
handle_simple_alert()
handle_confirm_alert_OK()
handle_confirm_alert_Cancel()
handle_modal_popup()