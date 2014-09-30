import unittest
from hamming import hamming


class HammingTests(unittest.TestCase):
  def test_empty_strings(self):
    self.assertEqual(
      0,
      hamming(u'', u'')
    )

  def test_one_nucleotide_same(self):
    self.assertEqual(
      0,
      hamming(u'A', u'A')
    )

  def test_one_nucleotide_different(self):
    self.assertEqual(
      1,
      hamming(u'A', u'G')
    )

  def test_short_nonequal(self):
    self.assertEqual(
      1,
      hamming(u'AT', u'CT')
    )

  def test_short_no_matches(self):
    self.assertEqual(
      2,
      hamming(u'AG', u'CT')
    )

  def test_long_nonequal(self):
    self.assertEqual(
      4,
      hamming(u'GGACGA', u'GGTCGA')
    )


