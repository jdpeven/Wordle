#!/usr/bin/env python3
from document_parser import DocumentParser
from game import Game

if __name__ == "__main__":
  while True:
    game = Game(DocumentParser())
    game.play_game()
    x = input('Play again? (y/n): ')
    if x != 'y':
      print("Thanks for playing!")
      break
