#!/usr/bin/env python3

from document_parser import DocumentParser

class Game():
  document_parser : DocumentParser
  secret_word : str
  attempts_allowed : int = 6
  guesses : list = []
  current_round : int = 1

  def __init__(self, document_parser: DocumentParser):
    self.document_parser = document_parser
    self.secret_word = document_parser.get_random_word()
  
  def play_game(self):
    while self.current_round < self.attempts_allowed:
      print('Round {0}'.format(self.current_round))
      self.print_guesses()
      guess : str
      while True:
        guess = input('Guess: ')
        if not guess.isalpha() or len(guess) != 5:
          print('Invalid input, try again')
          continue
        if not self.document_parser.is_valid_word(guess):
          print('Not in word list')
          continue
        break

      guess.lower()
      if guess == self.secret_word:
        print('success!')
        return    

      self.score_guess(guess)

      self.current_round += 1
    return

  def score_guess(self, guess: str):
    return

  def print_guesses(self):
    return