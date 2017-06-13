__author__ = 'jbernardin'

class Bar:

    def __init__(self, x):
        self.x = x
        self.x = None

    def some_method(self, y):
        return y if not self.x else self.x + y


if __name__ == '__main__':
    bar = Bar(3)
    print bar.some_method(5)