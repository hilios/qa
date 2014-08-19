import unittest, os


SRC_PATH = os.path.join(os.path.dirname(__file__), 'src')
TEST_CASES = unittest.defaultTestLoader.discover(SRC_PATH, '*.py')


suite = unittest.TestSuite()
suite.addTest(TEST_CASES)


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
