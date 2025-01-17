from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://webdriveruniversity.com/Data-Table/index.html")
driver.minimize_window()

# retrive total number of tables in selenium script
totalTable = driver.find_elements(By.TAG_NAME,'table')
print(len(totalTable))

# Total number of rows inside one table
total_rows = driver.find_elements(By.XPATH,'//*[@id="t01"]/tbody/tr')
print(len(total_rows))

# Total number of columns inside one row

totalColumsPerRow = driver.find_elements(By.XPATH,'//table[@id="t01"]/tbody/tr[2]/td')
print(totalColumsPerRow)

# //*[@id="t01"]/tbody/tr[4]/td[3]
total_sum = 0
for i in range(2,len(total_rows)+1):
    value  = int(driver.find_element(By.XPATH,f"//table[@id='t01']/tbody/tr[{i}]/td[3]").text)
    total_sum = total_sum + value
print(total_sum)

# try to find john in table 1

found = False
for i in range(2,len(total_rows)+1):
    name = (driver.find_element(By.XPATH,f"//table[@id='t01']/tbody/tr[{i}]/td[1]").text)
    if(name == "John"):
        print("found")
        found = True
        break
if not found:
    print("John was not found")


