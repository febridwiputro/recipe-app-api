"""
Sample tests
"""

from django.test import SimpleTestCase
import sys, os

# app_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
# sys.path.append(app_path)

from app import calc

class CalcTests(SimpleTestCase):

    """
    Test the calc module.
    """

    def test_add_numbers(self):
        res = calc.add(2, 4)

        self.assertEqual(res, 6)

    def test_substract_numbers(self):
        res = calc.substract(4, 2)

        self.assertEqual(res, 2)