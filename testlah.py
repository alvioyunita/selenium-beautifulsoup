from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (Chrome)
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.saucedemo.com/")

# Wait until input text 
WebDriverWait(driver, 2).until(
    EC.presence_of_element_located((By.ID, "user-name"))
)
# Find the search box
search_box = driver.find_element(By.NAME, "q")

# Type into the search box and press Enter
search_box.send_keys("Selenium WebDriver")
search_box.send_keys(Keys.RETURN)

# Wait to see results (optional)
driver.implicitly_wait(5)

# Check title contains search query
print("Page title:", driver.title)
assert "Selenium" in driver.title

# Close the browser
driver.quit()
