import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.google.com/")
        titleOfWebpage = driver.title

        #assertTrue
        self.assertTrue(titleOfWebpage == "Google")
        #assertFalse
        self.assertFalse(titleOfWebpage == "Google")


if __name__ == "__main__":
    unittest.main()