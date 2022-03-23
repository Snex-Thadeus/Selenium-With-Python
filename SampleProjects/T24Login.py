import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(executable_path=r"C:\Users\THADEUS ODHIAMBO\PycharmProjects\Selenium\drivers\chromedriver.exe")
driver.maximize_window()

driver.get("http://localhost:9095/BrowserWeb/servlet/BrowserServlet")
driver.find_element(By.XPATH, "//*[@id='signOnName']").send_keys("pdennis")
driver.find_element(By.XPATH, "//*[@id='password']").send_keys("Kenya123")
driver.find_element(By.ID, "sign-in").click()
time.sleep(5)

driver.switch_to.frame(1)

# driver.find_element(By.LINK_TEXT, "Sign Off").click()
driver.find_element(By.ID, "commandValue").send_keys("CUSTOMER, I F3 ")
driver.find_element(By.XPATH, "//*[@id='cmdline_img']").click()

# driver.find_element(By.XPATH, "//*[@id='pane_']/ul[1]/li/span").click()
# driver.find_element(By.XPATH, "//*[@id='pane_']/ul[1]/li/ul/li[1]/span").click()
# driver.find_element(By.XPATH, "//*[@id='pane_']/ul[1]/li/ul/li[1]/ul/li[1]/a").click()
time.sleep(5)

#Capture both window information
first = driver.window_handles[0]
second = driver.window_handles[1]
#switch to new window

driver.switch_to.window(second)
driver.maximize_window()

time.sleep(50)
driver.close()