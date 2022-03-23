import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.switch_to.frame("packageListFrame") # first frame
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
time.sleep(3)

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")  # second frame
driver.find_element(By.LINK_TEXT, "WebDriver").click()
time.sleep(3)

driver.switch_to.default_content()
time.sleep(3)
driver.switch_to.frame("classFrame") # third frame
driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[6]").click()

time.sleep(3)