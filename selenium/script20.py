from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
pages = driver.find_elements(By.CSS_SELECTOR,'ul#pagination > li')

for page in  pages:
    page.find_element(By.TAG_NAME,'a').click()
    rows = driver.find_elements(By.CSS_SELECTOR,"table#productTable tr")
   #  0   1  2  3  4  5
    #[r1,r2,r3,r4,r5,r6]
    for row in range(1,len(rows)):
       print(rows[row].text)
       rows[row].find_element(By.CSS_SELECTOR,"td:nth-child(4) input").click()
       







    time.sleep(0.5)
