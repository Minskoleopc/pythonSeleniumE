# java , python , javascript , html / css

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# get(String url)
#driver.get('https://webdriveruniversity.com/Contact-Us/contactus.html')
#driver.get('https://www.google.com')

# current_url
# driver.get('https://www.google.com')
# driver.find_element(By.CSS_SELECTOR,'[name="q"]').send_keys('python')
# driver.find_element(By.CSS_SELECTOR,'[name="q"]').send_keys(Keys.ENTER)
# print(driver.current_url)

# # title
# print(driver.title)
# if driver.title == 'python - Google Search':
#     print("test case pass")
# else:
#     print("test case fail")


#back()
driver.get('https://www.google.com')
driver.find_element(By.CSS_SELECTOR,'[name="q"]').send_keys('python')
driver.find_element(By.CSS_SELECTOR,'[name="q"]').send_keys(Keys.ENTER)



# if driver.title == 'python - Google Search':
#     print("test case pass")
# else:
#     print("test case fail")
# driver.back()
# if driver.title == "Google":
#     print('Test case pass')
# else:
#     print('Test case Fail')


# forward()
driver.back()
driver.forward()
if driver.title == 'python - Google Search':
    print("test case pass")
else:
    print("test case fail")


#driver.maximize_window()
