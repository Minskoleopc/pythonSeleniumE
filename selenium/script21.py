from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import configparser

# Set up the WebDriver (e.g., Chrome)

config = configparser.ConfigParser()
config.read('C:/Users/Lenovo/seleniumPython2024B/selenium/config.properties')

base_url = config.get("DEFAULT",'base_url')
username = config.get("USERS",'username')
password = config.get("USERS",'password')
print(base_url)
print(username)
brw = config.get("BROWSER",'brw')
if brw == "chrome":
    driver = webdriver.Chrome()
    driver.get(base_url)
    driver.find_element(By.ID,'user-name').send_keys(username)
    driver.find_element(By.ID,'password').send_keys(password)
    driver.find_element(By.ID,'login-button').click()



#driver = webdriver.Chrome()
