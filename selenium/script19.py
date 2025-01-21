from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the Datepicker page
driver.get("https://webdriveruniversity.com/Datepicker/index.html")

# Wait for the page to load
time.sleep(2)

# Locate the Datepicker input field and click to open the calendar
date_input = driver.find_element(By.ID, "datepicker")
date_input.click()

# Get the target date (381 days from today)
#future_date = datetime.today() + timedelta(days=381)
#print(future_date)
target_year = "2026" #future_date.year 
print(target_year )
target_month = "February" #future_date.strftime("%B")  # Full month name (e.g., "August")
print(target_month)
target_day = "6" #future_date.day
print(target_day)

#print(f"Target Date: {target_day} {target_month} {target_year}")

# Function to select the correct month and year
def select_month_and_year():
    while True:
        # Get current displayed month and year
        month_year_text = driver.find_element(By.CLASS_NAME, "datepicker-switch").text
        #print(f"Current Calendar Header: {month_year_text}")

        # If correct year and month, break the loop
        if target_month in month_year_text and str(target_year) in month_year_text:
            break
        
        # Click next button to go forward in months
        next_button = driver.find_element(By.CSS_SELECTOR, ".datepicker-days th.next")
        next_button.click()
        time.sleep(0.5)  # Small delay to let the UI update

# Function to select the correct day
def select_day():
    # Select the correct date
    day_element = driver.find_element(By.XPATH, f"//td[@class='day' and text()='{target_day}']")
    day_element.click()

# Perform the selection steps
select_month_and_year()
select_day()

# Get the selected date value
selected_date = date_input.get_attribute("value")
#print(f"Selected Date: {selected_date}")

# Close the browser
time.sleep(3)
driver.quit()
