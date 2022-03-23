from selenium import webdriver
import time
import HtmlTestRunner
import unittest
from SampleProjects.POMProject.pages.loginPage import LoginPage
from SampleProjects.POMProject.pages.homePage import Homepage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="C:/Users/THADEUS ODHIAMBO/PycharmProjects/Selenium/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_valid(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        # message = driver.find_element_by_xpath("").text
        # self.assertEqual(message,  "Invalid Credentials123")

        homepage = Homepage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()
        # self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element_by_link_text("Logout").click()
        time.sleep(2)

    # def test_02_login_invalid_username(self):
    #     driver = self.driver
    #
    #     driver.get("https://opensource-demo.orangehrmlive.com/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/THADEUS ODHIAMBO/PycharmProjects/Selenium/reports'))



