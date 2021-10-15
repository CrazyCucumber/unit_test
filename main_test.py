import unittest
from main import calc


class TestCalc(unittest.TestCase):

    def test_calc(self):
        self.assertEqual(calc(3, 2, '+'), 5)
        self.assertEqual(calc(3, 2, '*'), 6)
        self.assertEqual(calc(3, 2, '-'), 1)
        self.assertEqual(calc(1, 1, '+'), 2)
        self.assertEqual(calc(5, 3, '/'), 1.667)
        self.assertEqual(calc(3, 2, '/'), 1.5)

    def test_values(self):
        self.assertRaises(ValueError, calc, 1, 0, 'б')
