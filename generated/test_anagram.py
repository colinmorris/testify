import unittest
from anagram import detect_anagrams


class AnagramTests(unittest.TestCase):
  def test_no_matches(self):
    self.assertEqual(
      [],
      detect_anagrams(u'diaper', [u'hello', u'world', u'zombies', u'pants'])
    )

  def test_detects_simple_anagram(self):
    self.assertEqual(
      [u'tan'],
      detect_anagrams(u'ant', [u'tan', u'stand', u'at'])
    )


