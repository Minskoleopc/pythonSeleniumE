from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()
driver.get('https://webdriveruniversity.com/Contact-Us/contactus.html')

# locators 


findElement(driver,"form_buttons")

# By id 
#formButton =  driver.find_element(By.ID,"form_buttons")
# By Name 
headerElement = driver.find_element(By.NAME , "contactme")
print(headerElement.text)
if headerElement.text == "CONTACT US":
    print("test case pass")
else:
    print('test case fail')

# By ClassName
headerElementbyClassName = driver.find_element(By.CLASS_NAME,'section_header')
headerElementbyClassName.text
if headerElementbyClassName.text == "CONTACT US":
    print("test case pass")
else:
    print('test case fail')

# By TagName
textAreaElement = driver.find_element(By.TAG_NAME,'textarea')
if textAreaElement.is_displayed():
    print("test case pass")
else:
    print("test case fail")

# By xpath 
textAreaElementByXpath = driver.find_element(By.XPATH,'//*[@id="contact_form"]/textarea')
if textAreaElementByXpath.is_displayed():
    print("test case pass")
else:
    print("test case fail")

# By Css selector
textAreaElementByXpathCSSselector = driver.find_element(By.CSS_SELECTOR,'#contact_form > textarea')
if textAreaElementByXpathCSSselector.is_displayed():
    print("testcase pass")
else:
    print('testcase fail')



