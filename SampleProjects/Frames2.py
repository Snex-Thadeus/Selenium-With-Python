import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.NAME, "txtUsername").send_keys("Admin")
driver.find_element(By.NAME, "txtPassword").send_keys("admin123")
driver.find_element(By.NAME, "Submit").click()
