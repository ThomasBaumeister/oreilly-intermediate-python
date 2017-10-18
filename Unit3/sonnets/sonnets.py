#!/usr/bin/python3

import time

my_words = [elt.strip() for elt in open("sonnet_words.txt", "r").readlines()]
word_list = [elt.strip() for elt in open("sowpods.txt", "r").readlines()]
word_dict = dict((elt,1) for elt in open("sowpods.txt", "r").readlines())

counter = 0
start=time.time()
for word in my_words:
    if word not in word_dict:
        print(word)
        counter += 1
end=timeend=time.time()
print("Total new words: %d" % counter)
print("Total time: %.1f seconds" % (end - start) )
