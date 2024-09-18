"""
Sample test
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        result = calc.add(3, 4)
        self.assertEqual(result, 7)

    def test_subtract_numbers(self):
        result = calc.subtract(3, 4)
        self.assertEqual(result, -1)
