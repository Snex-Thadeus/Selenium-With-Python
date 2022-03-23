import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.google.com/")

        #assertIsNone
        self.assertIsNone(driver)
        #assertFalse
        self.assertIsNotNone(driver)


if __name__ == "__main__":
    unittest.main()