import unittest


class Test(unittest.TestCase):
    def testName(self):
        list = {"python", "selenium", "java"}

        #assertIn Is helpful when you want to verify presence of a value in a list, tuple,set dictionary
        self.assertIn("python", list)
        #assertNotIn
        self.assertNotIn("ruby", list)


if __name__ == "__main__":
    unittest.main()