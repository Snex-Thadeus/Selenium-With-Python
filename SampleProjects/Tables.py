import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("index.html")

rows = len(driver.find_elements(By.XPATH, "/html/body/table/tbody/tr")) # counts number of rows present
columns = len(driver.find_elements(By.XPATH, "/html/body/table/tbody/tr[1]/th")) # counts number of columns present

print(rows)
print(columns)

for r in range(2, rows+1):
    for c in range(1, columns+1):
        value = driver.find_elements(By.XPATH, "/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value, end='  ')
