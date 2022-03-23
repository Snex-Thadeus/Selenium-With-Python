import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://demo.guru99.com/test/newtours/")

print(driver.title)
print(driver.current_url)

time.sleep(5)

driver.close() # Closes one browser at a time / currently focused
driver.quit() # closes all the windows