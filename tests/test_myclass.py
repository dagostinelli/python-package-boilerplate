import unittest

from packagename.somemodule import MyClass

class TestMyClass(unittest.TestCase):

    def test_x(self):
        o = MyClass()
        self.assertEqual(o.x, 1)

    def test_y(self):
        o = MyClass()
        self.assertEqual(o.y, 2)

    def test_z(self):
        o = MyClass()
        self.assertEqual(o.z, 3)
