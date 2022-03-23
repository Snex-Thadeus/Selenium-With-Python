import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://jqueryui.com/datepicker/")

fr = driver.find_element(By.CLASS_NAME, "demo-frame")
driver.switch_to.frame(fr)

driver.find_element(By.ID, "datepicker").click()
driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()

driver.find_element(By.LINK_TEXT, "28").click()

time.sleep(5)
driver.quit()