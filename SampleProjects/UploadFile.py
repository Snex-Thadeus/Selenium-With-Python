import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

driver.switch_to.frame(0)

driver.find_element(By.ID, "RESULT_FileUpload-10").send_keys("E://logo.jpg")

time.sleep(5)