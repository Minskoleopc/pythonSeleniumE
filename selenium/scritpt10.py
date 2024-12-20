from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
import time

# get(String url)
driver.get('https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html')
dropdowns  = driver.find_elements(By.TAG_NAME,"select")
#[dr1,dr2,drp2]

# for dropdown in dropdowns:
#     select = Select(dropdown)
#     select.select_by_index(1)

for x in range(len(dropdowns)):
  select = Select(dropdowns[x])
  select.select_by_index(x)


checkboxes = driver.find_elements(By.CSS_SELECTOR,'input[type="checkbox"]')
for checkbox in checkboxes:
    # if checkbox.is_selected():
    #    pass
    # else:
    #    checkbox.click()
    if not checkbox.is_selected():
       checkbox.click()
       

radioButtons = driver.find_elements(By.CSS_SELECTOR,'#radio-buttons > input')   
for radioButton in radioButtons:
   radioButton.click()
   if radioButton.is_selected():
      print('test case pass')

       
       

time.sleep(3)
driver.quit()


