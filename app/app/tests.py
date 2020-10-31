from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):
    def test_add_numbers(self):
        """test that tow numbers are added together"""
        self.assertEqual(add(3, 7), 10)
  
    def test_subtract_numbers(self):
        """Test that values are subtracted and returned"""
        self.assertEqual(subtract(5, 11), 6)
        