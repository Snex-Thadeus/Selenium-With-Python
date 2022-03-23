import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

driver.maximize_window()

button = driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/p/span")

actions = ActionChains(driver)
actions.context_click(button).perform()

time.sleep(3)