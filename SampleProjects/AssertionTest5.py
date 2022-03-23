import unittest


class Test(unittest.TestCase):
    def testName(self):
        #AssertGreater
        self.assertGreater(100, 10)
        # AssertGreaterEqual
        self.assertGreaterEqual(100, 100)

        # AssertLess
        self.assertLess(10, 100)
        # AssertLessEqual
        self.assertLessEqual(100, 100)


if __name__ == "__main__":
    unittest.main()