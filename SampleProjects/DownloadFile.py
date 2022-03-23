import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


chromeOptions = Options
chromeOptions.add_experimental_option("prefs", {"download.default_directory": "C:/Users/THADEUS ODHIAMBO/Downloads"})

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chromeOptions)
driver.maximize_window()

driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.find_element(By.ID, "textbox").send_keys("Testing downloading textfile")

driver.find_element(By.ID, "createTxt").click()
driver.find_element(By.ID, "link-to-download").click()

time.sleep(3)