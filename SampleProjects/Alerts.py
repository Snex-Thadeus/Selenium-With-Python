import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://demo.guru99.com/test/newtours/")

driver.find_element(By.XPATH, "").click()

time.sleep(5)

driver.switch_to_alert().accept() # Closes alert window using OK button
driver.switch_to_alert().dismiss() # Closes alert window using Cancel button