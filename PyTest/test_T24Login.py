from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver = webdriver.Chrome(executable_path="C:/Users/THADEUS ODHIAMBO/PycharmProjects/Selenium/drivers/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()


def test_login(test_setup):
    driver.get("http://localhost:9095/BrowserWeb/servlet/BrowserServlet")
    driver.find_element(By.ID, "signOnName").send_keys("TEDDY1")
    driver.find_element(By.ID, "password").send_keys("Kenya1234")
    driver.find_element(By.ID, "sign-in").click()
    # x = driver.title
    # assert x == "OrangeHRM"


# def test_teardown():
#     driver.close()
#     driver.quit()

# for pytest the naming should be test_*.py