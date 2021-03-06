import unittest
from leap import isLeapYear


class LeapTests(unittest.TestCase):
  def test_a_known_leap_year(self):
    self.assertTrue(isLeapYear(1996))

  def test_any_old_year(self):
    self.assertFalse(isLeapYear(1997))

  def test_non_leap_even_year(self):
    self.assertFalse(isLeapYear(1998))

  def test_century(self):
    self.assertFalse(isLeapYear(1900))

  def test_exceptional_century(self):
    self.assertTrue(isLeapYear(2400))


