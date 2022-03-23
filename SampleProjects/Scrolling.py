import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.execute_script("window.scrollBy(0,1000)", "") # scroll by pixel

flag = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
driver.execute_script("arguments[0].scrollIntoView();", flag) # Scroll page till element is visible

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)") # Scroll till end of the page

time.sleep(5)