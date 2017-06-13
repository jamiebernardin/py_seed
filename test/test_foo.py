__author__ = 'jbernardin'


from app.foo import Foo
import unittest

class FooTest(unittest.TestCase):
    def setUp(self):
        self.foo = Foo(4)

    def test_hasX(self):
        self.assertNotEqual(self.foo.x, None, "Foo does not have x")


if __name__ == '__main__':
    unittest.main(verbosity=2)