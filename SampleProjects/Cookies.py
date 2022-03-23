from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.amazon.in/")

# Capture all the cookies created by browser
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# Add a new cookie to the browser
cookie = {'name': 'Mycookie', 'value': '1234567890'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# Deleting Cookie
driver.delete_cookie('Mycookie')
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)