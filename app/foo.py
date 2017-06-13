__author__ = 'jbernardin'


class Foo:

    def __init__(self, x):
        self.x = x
        self.x = None

    def some_method(self, y):
        return self.x + y


if __name__ == '__main__':
    foo = Foo(3)
    print foo.some_method(5)