# -*- coding: utf-8 -*-
from selenium import webdriver
import HtmlTestRunner
import unittest, time


class AuthorizeTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'..\drivers\chromedriver.exe')
        cls.driver.implicitly_wait(10)
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://localhost:9095/BrowserWeb/servlet/BrowserServlet")
        driver.find_element_by_id("signOnName").click()
        driver.find_element_by_id("signOnName").clear()
        driver.find_element_by_id("signOnName").send_keys("TEDDY1")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("Kenya1234")
        driver.find_element_by_id("sign-in").click()
        driver.maximize_window()

        driver.switch_to.frame(1)
        driver.find_element_by_xpath("//span[@onclick='ProcessMouseClick(event)']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='pane_']/ul/li/ul/li/span").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='pane_']/ul[1]/li/ul/li[1]/ul/li[7]/a").click()
        # Capture both window information
        first = driver.window_handles[0]
        second = driver.window_handles[1]
        #ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=//div[@id='pane_']/ul/li/ul/li/span | ]]
        driver.find_element_by_link_text("Authorise/Delete Customer").click()
        driver.switch_to.window(second)
        #ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        # driver.find_element_by_xpath("//img[@alt='Delete']").click()
        # time.sleep(2)
        # driver.find_element_by_xpath("//img[@alt='Deletes a Deal']").click()
        # time.sleep(2)
        # driver.find_element_by_xpath("//img[@alt='Refresh']").click()
        # time.sleep(2)
        driver.find_element_by_xpath("//img[@alt='Authorise']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//img[@alt='Authorises a deal']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//img[@alt='Refresh']").click()
        time.sleep(2)
        # driver.close()
        driver.switch_to.window(first)
        driver.switch_to.frame(0)
        #ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
        #ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_link_text("Sign Off").click()

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Selenium/reports'), verbosity=2)
