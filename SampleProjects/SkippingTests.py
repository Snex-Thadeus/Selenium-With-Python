import unittest


class AppTesting(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):
        print("This is search test")

    @unittest.skip("I am skipping this test method because its not ready yet")
    def test_advancedsearch(self):
        print("This is Advanced search test")

    @unittest.skipIf(1==1, "It's true")
    def test_prepaidRecharge(self):
        print("This prepaid Recharge test")

    def test_postRecharge(self):
        print("This post Recharge test")

    def test_loginbygmail(self):
        print("This login by gmail")

    def test_loginbytwitter(self):
        print("This login by twitter")


if __name__ == "__main__":
    unittest.main()