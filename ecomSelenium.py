import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Initialize webdriver
driver = webdriver.Chrome('/Users/I527241/Downloads/chromedriver_mac64/chromedriver')

# Open nopCommerce Demo Store
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()

# Click on the Register button
register_button = driver.find_element(By.LINK_TEXT, 'Register')
register_button.click()

# Fill in the registration form
time.sleep(2)  # Wait for the page to load
first_name = driver.find_element(By.ID, 'FirstName')
first_name.send_keys('John')

last_name = driver.find_element(By.ID, 'LastName')
last_name.send_keys('Doe')

email = driver.find_element(By.ID, 'Email')
email.send_keys('johndoe@example.com')

password = driver.find_element(By.ID, 'Password')
password.send_keys('password')

confirm_password = driver.find_element(By.ID, 'ConfirmPassword')
confirm_password.send_keys('password')

register_button = driver.find_element(By.ID, 'register-button')
register_button.click()

# Wait for the registration success message
time.sleep(2)

# Search for a product
search_box = driver.find_element(By.ID, 'small-searchterms')
search_box.send_keys('laptop')  # Replace with the desired product to search
search_box.send_keys(Keys.RETURN)

# Wait for search results
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.product-item')))

# Click on the first search result (image)
first_result_image = driver.find_element(By.CSS_SELECTOR, '.product-item .picture img')
first_result_image.click()

# Wait for the product page to load
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#product-details')))

# Close the browser
driver.quit()
