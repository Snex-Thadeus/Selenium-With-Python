import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://demo.guru99.com/test/newtours/")

links = driver.find_elements(By.TAG_NAME, "a")
print(len(links)) # How many links present in a page

for link in links:
    print(link.text)

# Clicking on the link
# driver.find_element(By.LINK_TEXT, "REGISTER").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "REG").click()