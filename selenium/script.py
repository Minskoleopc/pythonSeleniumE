from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

try:
    # Open a webpage
    driver.get("https://www.google.com")

    # Find the search box using its name attribute
    search_box = driver.find_element(By.NAME, "q")

    # Type a query and hit Enter
    search_box.send_keys("Selenium Python" + Keys.RETURN)

    # Wait for the results to load and display the title
    print(driver.title)
finally:
    # Close the browser
    driver.quit()
