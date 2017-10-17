#!/usr/bin/python3

import string
import scrabble

for letter in string.ascii_lowercase:
  exists=False
  for word in scrabble.wordlist:
    if letter*2   in word:
      exists=True
      break
  if not exists:
    print("There is no english word with the double letter " + letter)

