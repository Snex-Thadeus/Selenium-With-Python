import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class SearchEngine(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.google.com/")
        print(self.driver.title)
        self.driver.close()

    def test_Bing(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.bing.com/")
        print(self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()