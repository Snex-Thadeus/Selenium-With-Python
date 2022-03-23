import XLUtils
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://demo.guru99.com/test/newtours/index.php")

driver.maximize_window()

path = "E:/Login.xlsx"

rows = XLUtils.getRowCount(path, 'Sheet1')

for r in range(2, rows+1):
    username = XLUtils.readData(path, "Sheet1", r, 1)
    password = XLUtils.readData(path, "Sheet1", r, 2)

    driver.find_element(By.NAME, "userName").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "submit").click()

    if driver.title == "Login: Mercury Tours":
        print("Test is passed")
        XLUtils.writeData(path, "Sheet1", r, 3, "Test Passed")
    else:
        print("Test failed")
        XLUtils.writeData(path, "Sheet1", r, 3, "Test Failed")

    driver.find_element(By.LINK_TEXT, "Home").click()