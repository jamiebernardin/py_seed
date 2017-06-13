__author__ = 'jbernardin'

from app.bar import Bar
import unittest

class BarTest(unittest.TestCase):
    def setUp(self):
        self.bar = Bar(4)

    def test_hasX(self):
        self.assertIsNotNone(self.bar.x, "x is None")

    def test_someMethod(self):
        self.assertIs(self.bar.some_method(5), 9, "wrong result for someMethod")


if __name__ == '__main__':
    unittest.main(verbosity=2)