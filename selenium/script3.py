from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# webdriver 
# weblements - methods
driver = webdriver.Chrome()
driver.get('https://webdriveruniversity.com/Contact-Us/contactus.html')

firstNameElement = driver.find_element(By.NAME,"first_name")
#<input name="first_name" type="text" class="feedback-input" placeholder="First Name">

#click()
#firstNameElement.click()

#send_keys()
driver.find_element(By.NAME,"first_name").send_keys("chinmay")

#clear()
driver.find_element(By.NAME,"first_name").clear()

#get_attribute()
classValue = driver.find_element(By.NAME,"first_name").get_attribute('class')
print(classValue)

#element text - property
#<h2 name="contactme" class="section_header">CONTACT US</h2>
text = driver.find_element(By.NAME,'contactme').text
print(text)

