import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

element = driver.find_element(By.XPATH, "//*[@id='HTML10']/div[1]/button")

actions = ActionChains(driver)
actions.double_click(element).perform()

time.sleep(3)