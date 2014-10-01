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

  def test_does_not_confuse_different_duplicates(self):
    self.assertEqual(
      [],
      detect_anagrams(u'galea', [u'eagle'])
    )

  def test_eliminates_anagram_subsets(self):
    self.assertEqual(
      [],
      detect_anagrams(u'good', [u'dog', u'goody'])
    )

  def test_detects_multiple_anagrams(self):
    self.assertEqual(
      [u'gallery', u'regally', u'largely'],
      detect_anagrams(u'allergy', [u'gallery', u'ballerina', u'regally', u'clergy', u'largely', u'leading'])
    )

  def test_same_word_isnt_anagram(self):
    self.assertEqual(
      [],
      detect_anagrams(u'banana', [u'banana'])
    )

  def test_is_case_insensitive(self):
    self.assertEqual(
      [u'Orchestra'],
      detect_anagrams(u'Orchestra', [u'cashregister', u'Carthorse', u'radishes'])
    )


