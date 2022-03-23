from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://demo.guru99.com/test/newtours/index.php")

# driver.save_screenshot("E:/UntitledTestSuite/homepage.png")

driver.get_screenshot_as_file("E:/UntitledTestSuite/homepage.png") # shoil end with a .png extension