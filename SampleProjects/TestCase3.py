import unittest


def setupmodule(): # will be executed before executing any class or any method present in test class
    print("setUpModule")


def tearupmodule(): # will be executed before executing any class or any method present in test class
    print("tearUpModule")


class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self): # Execute before starting of every test method
        print("This is login test")

    @classmethod
    def tearDown(self): # Execute after completion of every test method
        print("This is logout test")

    @classmethod
    def setUpClass(cls):  # Execute once when the class started
        print("Opening application")

    @classmethod
    def tearDownClass(cls):  # Executed once when the class is completed
        print("Close application")

    def test_search(self):
        print("This is search test")

    def test_advancedsearch(self):
        print("This is Advanced search test")

    def test_prepaidRecharge(self):
        print("This prepaid Recharge test")

    def test_postRecharge(self):
        print("This post Recharge test")


if __name__ == "__main__":
    unittest.main()
