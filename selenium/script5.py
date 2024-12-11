from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()
driver.get('https://webdriveruniversity.com/Contact-Us/contactus.html')

# Webelement methods 
# click(), submit() , sendkeys() , clear() ,getAttribute()
# isenabled() , isdisplayed(), isSelected(), tagName , text

contactme = driver.find_element(By.NAME,"contactme")
#contactme.screenshot('header.png')
#print(contactme.location)
#print(contactme.size)
#print(contactme.rect)
#print(contactme.tag_name)
e = contactme.value_of_css_property('font-family')
print(e)

driver.close()

