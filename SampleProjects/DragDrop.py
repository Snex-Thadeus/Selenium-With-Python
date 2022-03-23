import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("")
driver.maximize_window()

source_element = driver.find_element(By.XPATH, "//*[@id='box6'")
target_element = driver.find_element(By.XPATH, "//*[@id='box10'")

actions = ActionChains(driver)

actions.drag_and_drop(source_element, target_element).perform()

time.sleep(3)