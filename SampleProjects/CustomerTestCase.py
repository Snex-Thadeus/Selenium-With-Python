# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\THADEUS ODHIAMBO\PycharmProjects\Selenium\drivers\chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://localhost:9095/BrowserWeb/servlet/BrowserServlet")
        driver.find_element_by_id("signOnName").clear()
        driver.find_element_by_id("signOnName").send_keys("pdennis")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("Kenya123")
        driver.find_element_by_id("sign-in").click()
        driver.maximize_window()
        driver.switch_to.frame(1)
        #ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.find_element_by_xpath("//span[@onclick='ProcessMouseClick(event)']").click()
        driver.find_element_by_xpath("//div[@id='pane_']/ul/li/ul/li/span").click()
        driver.find_element_by_link_text("Individual Customer").click()
        # Capture both window information
        first = driver.window_handles[0]
        second = driver.window_handles[1]
        # switch to new window

        driver.switch_to.window(second)
        driver.maximize_window()
        #ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        driver.find_element_by_id("fieldName:TITLE").click()
        Select(driver.find_element_by_id("fieldName:TITLE")).select_by_visible_text("Mr.")
        driver.find_element_by_id("fieldName:GIVEN.NAMES").click()
        driver.find_element_by_id("fieldName:GIVEN.NAMES").clear()
        driver.find_element_by_id("fieldName:GIVEN.NAMES").send_keys("SAMUEL")
        driver.find_element_by_id("fieldName:FAMILY.NAME").click()
        driver.find_element_by_id("fieldName:FAMILY.NAME").clear()
        driver.find_element_by_id("fieldName:FAMILY.NAME").send_keys("WESONGA")
        driver.find_element_by_id("fieldName:NAME.1:1").click()
        driver.find_element_by_id("fieldName:NAME.1:1").clear()
        driver.find_element_by_id("fieldName:NAME.1:1").send_keys("SAMUEL WESONGA")
        driver.find_element_by_id("fieldName:SHORT.NAME:1").click()
        driver.find_element_by_id("fieldName:SHORT.NAME:1").clear()
        driver.find_element_by_id("fieldName:SHORT.NAME:1").send_keys("SAM")
        driver.find_element_by_id("fieldName:MNEMONIC").click()
        driver.find_element_by_id("fieldName:MNEMONIC").clear()
        driver.find_element_by_id("fieldName:MNEMONIC").send_keys("SAMY")
        driver.find_element_by_xpath("//table[@id='mainTab']/tbody/tr[7]/td[3]/table/tbody/tr/td[2]/input").click()
        driver.find_element_by_id("fieldName:ACCOUNT.OFFICER").click()
        driver.find_element_by_id("fieldName:ACCOUNT.OFFICER").clear()
        driver.find_element_by_id("fieldName:ACCOUNT.OFFICER").send_keys("1")
        driver.find_element_by_id("fieldName:SECTOR").click()
        driver.find_element_by_id("fieldName:SECTOR").clear()
        driver.find_element_by_id("fieldName:SECTOR").send_keys("1001")
        driver.find_element_by_xpath("//body").click()
        driver.find_element_by_id("fieldName:CUSTOMER.TYPE").click()
        Select(driver.find_element_by_id("fieldName:CUSTOMER.TYPE")).select_by_visible_text("ACTIVE")
        driver.find_element_by_xpath("//table[@id='mainTab']/tbody/tr[15]/td[3]/a/img").click()
        driver.find_element_by_link_text("13").click()
        driver.find_element_by_id("fieldName:STREET:1").click()
        driver.find_element_by_id("fieldName:STREET:1").clear()
        driver.find_element_by_id("fieldName:STREET:1").send_keys("KAKAMEGA, KENYA")
        driver.find_element_by_id("fieldName:TOWN.COUNTRY:1").click()
        driver.find_element_by_id("fieldName:TOWN.COUNTRY:1").clear()
        driver.find_element_by_id("fieldName:TOWN.COUNTRY:1").send_keys("KAKAMEGA")
        driver.find_element_by_id("fieldName:POST.CODE:1").click()
        driver.find_element_by_id("fieldName:POST.CODE:1").clear()
        driver.find_element_by_id("fieldName:POST.CODE:1").send_keys("50402")
        driver.find_element_by_id("fieldName:COUNTRY:1").click()
        driver.find_element_by_id("fieldName:COUNTRY:1").clear()
        driver.find_element_by_id("fieldName:COUNTRY:1").send_keys("KENYA")
        driver.find_element_by_id("tab1").click()
        driver.find_element_by_id("fieldName:PHONE.1:1").click()
        driver.find_element_by_id("fieldName:PHONE.1:1").clear()
        driver.find_element_by_id("fieldName:PHONE.1:1").send_keys("0789765757")
        driver.find_element_by_id("fieldName:EMAIL.1:1").click()
        driver.find_element_by_id("fieldName:EMAIL.1:1").clear()
        driver.find_element_by_id("fieldName:EMAIL.1:1").send_keys("sam254@gmail.com")
        driver.find_element_by_xpath("//img[@alt='Commit the deal']").click()
        driver.find_element_by_id("warningChooser:Have you received Copy of Social Security Card/CUS*502 from 111574").click()
        Select(driver.find_element_by_id("warningChooser:Have you received Copy of Social Security Card/CUS*502 from 111574")).select_by_visible_text("RECEIVED")
        driver.find_element_by_xpath("//img[@alt='Commit the deal']").click()
        driver.close()
        #ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
        #ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_link_text("Sign Off").click()
        #ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_id("signOnName").clear()
        driver.find_element_by_id("signOnName").send_keys("TEDDY1")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("Kenya1234")
        driver.find_element_by_id("sign-in").click()
        #ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.find_element_by_xpath("//span[@onclick='ProcessMouseClick(event)']").click()
        driver.find_element_by_xpath("//div[@id='pane_']/ul/li/ul/li/span").click()
        driver.find_element_by_link_text("Authorise/Delete Customer").click()
        #ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_2 | ]]
        driver.find_element_by_xpath("//img[@alt='Authorise']").click()
        driver.find_element_by_xpath("//img[@alt='Authorises a deal']").click()
        driver.find_element_by_xpath("//img[@alt='Refresh']").click()
        driver.close()
        #ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
        #ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_link_text("Sign Off").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
