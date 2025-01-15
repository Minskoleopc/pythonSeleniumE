from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://dev.automationtesting.in/shadow-dom")

# Example 1: Access the first Shadow DOM element
shadow_host_1 = driver.find_element(By.CSS_SELECTOR, "#shadow-root")  
shadow_root_1 = shadow_host_1.shadow_root 
shadow_element_1 = shadow_root_1.find_element(By.CSS_SELECTOR, "#shadow-element")  # Replace with actual selector
print(shadow_element_1.text)

shadow_host_2 = shadow_root_1.find_element(By.CSS_SELECTOR,'#inner-shadow-dom')
shadow_root_2 = shadow_host_2.shadow_root 
nested_shadow_element = shadow_root_2.find_element(By.CSS_SELECTOR, "#nested-shadow-element")
print(nested_shadow_element.text)

shadow_host_3 = shadow_root_2.find_element(By.CSS_SELECTOR,'#nested-shadow-root')
shadow_root_3 = shadow_host_3.shadow_root
shadow_root_3 .find_element(By.CSS_SELECTOR, "#nested-shadow-dom")
ele3 = shadow_root_3 .find_element(By.CSS_SELECTOR, "#multi-nested-shadow-element")
print(ele3.text)

driver.quit()
# DOM ===> element(shadowhost) ====> shadowRoot ==> (element , element(host))