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
      {u'of': 1, u'each': 1, u'one': 1},
      word_count(u'one of each')
    )

  def test_counts_multiple_occurences(self):
    self.assertEqual(
      {u'blue': 1, u'fish': 4, u'two': 1, u'red': 1, u'one': 1},
      word_count(u'one fish two fish red fish blue fish')
    )

  def test_preserves_punctuation(self):
    self.assertEqual(
      {u'java': 1, u'javascript!!&@$%^&': 1, u'car': 1, u'as': 1, u':': 2, u'carpet': 1},
      word_count(u'car : carpet as java : javascript!!&@$%^&')
    )

  def test_includes_numbers(self):
    self.assertEqual(
      {u'1': 1, u'2': 1, u'testing': 2},
      word_count(u'testing 1 2 testing')
    )

  def test_preserves_mixed_case(self):
    self.assertEqual(
      {u'go': 1, u'Go': 1, u'GO': 1},
      word_count(u'Go go GO')
    )

  def test_multiple_spaces(self):
    self.assertEqual(
      {u'it': 1, u'for': 1, u'wait': 1},
      word_count(u'wait for     it')
    )

  def test_splits_on_newlines(self):
    self.assertEqual(
      {u'ma': 1, u'want': 1, u'oh': 1, u'ah': 3, u'la': 2, u'rah': 2, u'romance': 1, u'bad': 1, u'ga': 2, u'roma': 2, u'your': 1},
      word_count(u'rah rah ah ah ah\nroma roma ma\nga ga oh la la\nwant your bad romance')
    )


