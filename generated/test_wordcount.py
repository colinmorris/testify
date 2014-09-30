import unittest
from wordcount import word_count


class WordcountTests(unittest.TestCase):
  def test_counts_one_word(self):
    self.assertEqual(
      {u'word': 1},
      word_count(u'word')
    )

  def test_counts_one_of_each(self):
    self.assertEqual(
      {u'word': 1},
      word_count(u'word')
    )


