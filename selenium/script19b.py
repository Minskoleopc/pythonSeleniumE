from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://webdriveruniversity.com/Datepicker/index.html")
driver.maximize_window()

driver.find_element(By.ID,'datepicker').click()
future_year = "2026"
future_month = "March"
furture_date = "14"


def select_month_year():
    while True:
        month_year = driver.find_element(By.CSS_SELECTOR,'.datepicker-switch').text
        if( future_month in month_year and future_year in month_year):
            break
        driver.find_element(By.CSS_SELECTOR,'th.next').click()
        time.sleep(0.5)


def select_day():
    #driver.find_element(By.XPATH,f"//td[class='day' and text()='{furture_date}']")
    days = driver.find_elements(By.CLASS_NAME,"day")
    for day in days:
        if day.text == furture_date:
            day.click()
            break


select_month_year()
select_day()
time.sleep(3)

