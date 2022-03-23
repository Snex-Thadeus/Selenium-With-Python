import unittest


class LoginTest(unittest.TestCase):
    def test_LoginbyEmail(self):
        print("This is login by email test")
        self.assertTrue(True)

    def test_LoginbyFacebook(self):
        print("This is login by facebook test")
        self.assertTrue(True)

    def test_LoginbyTwitter(self):
        print("This is login by twitter test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()