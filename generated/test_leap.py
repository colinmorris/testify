import unittest
from leap import isLeapYear


class LeapTests(unittest.TestCase):
  def test_a_known_leap_year(self):
    self.assertEqual(
      True,
      isLeapYear(1996)
    )

  def test_any_old_year(self):
    self.assertEqual(
      False,
      isLeapYear(1997)
    )


