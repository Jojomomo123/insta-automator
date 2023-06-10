from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Configure the WebDriver
driver = webdriver.Chrome(r'C:\Users\joshu\Downloads\chromedriver_win32 (11)\chromedriver.exe')  # Replace with the actual path to your ChromeDriver executable

# Open Instagram
driver.get('https://www.instagram.com/')

# Perform automation tasks
time.sleep(2)  # Wait for the page to load
username_field = driver.find_element('username')  # Find the username field
password_field = driver.find_element_by_name('password')  # Find the password field

username_field.send_keys('your_username')  # Replace with your Instagram username
password_field.send_keys('your_password')  # Replace with your Instagram password

login_button = driver.find_element_by_css_selector('button[type="submit"]')  # Find the login button
login_button.click()  # Click the login button

time.sleep(5)  # Wait for the login process

# Close the browser
driver.quit()