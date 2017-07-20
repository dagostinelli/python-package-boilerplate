import unittest

from packagename.somemodule import MySecondClass

class TestMySecondClass(unittest.TestCase):

    def test_p(self):
        o = MySecondClass()
        self.assertEqual(o.p, 1)

    def test_d(self):
        o = MySecondClass()
        self.assertEqual(o.d, 2)

    def test_q(self):
        o = MySecondClass()
        self.assertEqual(o.q, 3)
