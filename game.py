#!/usr/bin/env python3

from document_parser import DocumentParser

class Game():
  document_parser : DocumentParser
  secret_word : str
  attempts_allowed : int = 6
  guesses : list = []
  guesses_score : list = []
  current_round : int = 1
  characters_not_in_word : list = []
  characters_in_word : list = []
  outline : list = []

  def __init__(self, document_parser: DocumentParser):
    self.document_parser = document_parser
    self.secret_word = document_parser.get_random_word()
    self.guesses = []
    self.guesses_score = []
    self.current_round = 1
    self.characters_not_in_word = []
    self.characters_in_word = []
    self.outline = ["_", "_", "_", "_", "_"]
  
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
    
    print('Sorry! Word was {0}'.format(self.secret_word))

  def score_guess(self, guess: str):
    score = ''
    for i in range(len(self.secret_word)):
      if guess[i] == self.secret_word[i]:
        score += 'M '
        self.outline[i] = guess[i]
        if guess[i] not in self.characters_in_word:
          self.characters_in_word.append(guess[i])
        continue
      if guess[i] in self.secret_word:
        score += 'X '
        if guess[i] not in self.characters_in_word:
          self.characters_in_word.append(guess[i])
        continue
      if guess[i] not in self.characters_not_in_word:
        self.characters_not_in_word += guess[i]
      score += '_ '
    
    self.guesses.append(guess)
    self.guesses_score.append(score)
    self.characters_not_in_word.sort()
    self.characters_in_word.sort()

  def print_guesses(self):
    print('M: Character in correct location')
    print('X: Character in the word somewhere else')
    for i in range(len(self.guesses)):
      print("{0}: {1}".format(self.guesses[i], self.guesses_score[i]))
    
    print('Characters not in word')
    print(self.characters_not_in_word)
    print('Characters in word')
    print(self.characters_in_word)
    
    print(self.outline)
      