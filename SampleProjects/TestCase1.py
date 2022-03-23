import unittest
import HtmlTestRunner


class Test(unittest.TestCase):

    def test_firstTest(self):
        print("This is my first unit testcase")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Selenium/reports'), verbosity=2)