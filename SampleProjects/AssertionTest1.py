import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.google.com/")
        titleOfWebpage = driver.title

        #assertEqual
        # self.assertEqual("Google", titleOfWebpage, "Webpage title not the same")
        #assertEqual
        self.assertNotEqual("Google", titleOfWebpage, "Webpage title not the same")


if __name__ == "__main__":
    unittest.main()