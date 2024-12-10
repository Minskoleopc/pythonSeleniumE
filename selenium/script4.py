from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()
driver.get('https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html')

# is_displayed()

headerElement = driver.find_element(By.XPATH, '//*[@id="main-header"]/h1')
if headerElement.is_displayed():
    print("testcase pass")
else:
    print("testcase fail")

# is_enabled()

cabbageELement = driver.find_element(By.CSS_SELECTOR,'input[name="vegetable"][value="cabbage"]')
if cabbageELement.is_enabled():
    print("test case fail ...")
else:
    print('test case pass ...')

# isSelected()
pumpkinElement = driver.find_element(By.CSS_SELECTOR,'input[name="vegetable"][value="pumpkin"]')
if pumpkinElement.is_selected():
    print("test case pass ......")
else:
    print("test case fail ......")

# tagName()
e = pumpkinElement.tag_name
print(e)