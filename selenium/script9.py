from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()

# get(String url)
driver.get('https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html')

# select by visible text 
# select by value 
# select by index

# find drop down element
dropdwn_element = driver.find_element(By.ID,'dropdowm-menu-1')
dropDown = Select(dropdwn_element)
dropDown.select_by_index(1)
dropDown.select_by_value('java')
dropDown.select_by_visible_text('Python')

#checkbox testcase 
element3 = driver.find_element(By.CSS_SELECTOR,"input[type= 'checkbox'][value='option-3']")
if element3.is_selected():
    print("testcase pass")
else:
    print('testcase fail')

element2 = driver.find_element(By.CSS_SELECTOR,"input[type= 'checkbox'][value='option-2']")
element2.click()
if element2.is_selected():
    print("test case pass 2")
else:
    print("test case fail")

# radio button testcase 
greenElement = driver.find_element(By.CSS_SELECTOR,"input[value='green']")
redElement = driver.find_element(By.CSS_SELECTOR,"input[value='blue']")

greenElement.click()
if greenElement.is_selected() and redElement.is_selected() == False :
    print("test case pass")
else:
    print('test case fail')