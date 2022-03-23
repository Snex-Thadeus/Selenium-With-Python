import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element(By.XPATH, "//*[@id='Tabbed']/a/button").click()

driver.current_window_handle  # parent window\
handles = driver.window_handles # return all the handle values of open windows

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close() # closes only the parent window

driver.quit()