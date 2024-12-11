from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# webdriver 
driver = webdriver.Chrome()
driver.get('https://webdriveruniversity.com/Contact-Us/contactus.html')

# submit()

driver.find_element(By.NAME,"first_name").send_keys("chinmay")
driver.find_element(By.NAME,"last_name").send_keys("deshpande")
driver.find_element(By.NAME,"email").send_keys("chinmaydeshpande010@gmail.com")
driver.find_element(By.NAME,"message").send_keys("learning js")
driver.find_element(By.ID,'contact_form').submit()
driver.quit()