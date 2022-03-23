import unittest


class SignupTest(unittest.TestCase):
    def test_SignbyEmail(self):
        print("This is Sign by email test")
        self.assertTrue(True)

    def test_SignbyFacebook(self):
        print("This is Sign by facebook test")
        self.assertTrue(True)

    def test_SignbyTwitter(self):
        print("This is Sign by twitter test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()