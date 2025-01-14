# how to find broken links in selenium- python
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()
driver.get('https://webdriveruniversity.com/')

# Find all the links on the page 
links = driver.find_elements(By.TAG_NAME,'a')
for link in links:
    url = link.get_attribute('href')
    if url is not None and url.startswith('https'):
        try:
            response = requests.head(url,allow_redirects=True)
            if response.status_code >= 400:
                print(f"Broken link:{url}") 
            else:
                 print(f"Valid link:{url}") 
        except requests.RequestException as e:
            print(f"Exception:{e}") 

driver.quit()
           
