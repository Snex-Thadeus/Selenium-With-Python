import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://demo.guru99.com/test/newtours/reservation.php")

drp = Select(driver.find_element(By.NAME, "fromPort"))

# drp.select_by_visible_text("Paris")
# drp.select_by_index(2)
# drp.select_by_value("Seattle")

# Count number of options
print(len(drp.options))

# Capture all the options from the dropdown
all_options = drp.options

for option in all_options:
    print(option.text)

time.sleep(5)