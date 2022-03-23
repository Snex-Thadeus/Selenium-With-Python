from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://demo.guru99.com/test/newtours/")

driver.implicitly_wait(10)

assert "Welcome: Mercury Tours" in driver.title

user_ele = driver.find_element(By.NAME, "userName")
pwd_ele = driver.find_element(By.NAME, "password")

user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")

driver.find_element(By.NAME, "submit").click()