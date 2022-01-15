#!/usr/bin/env python3
import random

class DocumentParser():
  file_name : str
  words : set

  def __init__(self):
    self.file_name = "data/words.txt"
    self.words = set(self._get_words())

  def _get_words(self) -> list:
    f = open(self.file_name, "r")
    words = f.read().splitlines()
    f.close()
    return words

  def get_random_word(self) -> str:
    return random.sample(self.words, 1)

  def is_valid_word(self, word) -> bool:
    return word in self.words
