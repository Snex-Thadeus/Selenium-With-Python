from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://demo.guru99.com/test/newtours/")

user_ele = driver.find_element(By.NAME, "userName")
print(user_ele.is_displayed())
print(user_ele.is_enabled())

pwd_ele = driver.find_element(By.NAME, "password")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")

driver.find_element(By.NAME, "submit").click()

driver.find_element(By.LINK_TEXT, "Flights").click()

roundtrip_radio = driver.find_element(By.CSS_SELECTOR, "input[value=roundtrip]")
print(roundtrip_radio.is_selected())

onetrip_radio = driver.find_element(By.CSS_SELECTOR, "input[value=oneway]")
print(onetrip_radio.is_selected())