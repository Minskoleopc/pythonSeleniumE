from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()
driver.get('https://webdriveruniversity.com/')
#driver.find_element(By.LINK_TEXT,"CONTACT US")
driver.find_element(By.PARTIAL_LINK_TEXT,"CONTACT")