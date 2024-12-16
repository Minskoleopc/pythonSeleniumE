
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

# get(String url)
driver.get('https://webdriveruniversity.com')
driver.find_element(By.CSS_SELECTOR,'#contact-us').click()
driver.find_element(By.CSS_SELECTOR,'#login-portal').click()
driver.find_element(By.CSS_SELECTOR,'#button-clicks').click()


# only switching to one handle
# print(driver.title)
# print(driver.title)
# handles = driver.window_handles
# print(handles)
# driver.switch_to.window(handles[1])
# print(driver.title)
# driver.switch_to.window(handles[2])
# print(driver.title)
# if driver.find_element(By.NAME,'contactme').is_displayed():
#     print("test case pass")
# else:
#     print("test case fail")

# get all tabs title 

handles = driver.window_handles
for x in handles:
   driver.switch_to.window(x)
   print(driver.title)