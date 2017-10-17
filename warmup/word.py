#!/usr/bin/python3

import scrabble

for word in scrabble.wordlist: 
  if "uu" in word:
    print(word)
