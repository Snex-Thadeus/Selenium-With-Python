import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.implicitly_wait(5)

driver.maximize_window()

driver.get("https://www.expedia.com/")

driver.find_element(By.LINK_TEXT, "Flights").click()
time.sleep(2)

driver.find_element(By.ID, "location-field-leg1-origin").send_keys("NAIROBI")
driver.find_element(By.XPATH, "//*[@id='location-field-leg1-origin-menu']/div[2]/div[2]/ul/li/button").click()
time.sleep(2)

driver.find_element(By.ID, "location-field-leg1-destination").send_keys("DUBAI")
driver.find_element(By.XPATH, "//*[@id='location-field-leg1-destination-menu']/div[2]/div[2]/ul/li[1]/button").click()

driver.find_element(By.ID, "d1-btn").click()
driver.find_element(By.XPATH, "//*[@id='wizard-flight-tab-roundtrip']/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/table/tbody/tr[2]/td[5]/button").send_keys("10/04/2022")

driver.find_element(By.XPATH, "//*[@id='wizard-flight-tab-roundtrip']/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[3]/button").send_keys("15/04/2022")

driver.find_element(By.XPATH, "//*[@id='wizard-flight-tab-roundtrip']/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[3]/button").click()
driver.find_element(By.XPATH, "//*[@id='wizard-flight-pwa-1']/div[3]/div[2]/button").click()

# Explicit waits
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stops-0']")))
element.click()

time.sleep(3)

driver.quit()