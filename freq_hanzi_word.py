#!/usr/bin/python
#coding=utf-8

import sys
import re
import os
import jieba
from string import punctuation
from operator import itemgetter

sys.path.append("../")
default_encoding='utf-8'

N = 1000
words = {}

with open(sys.argv[1]) as file: 
	text = file.read()
	words_gen = jieba.cut(text)

with open("easy_words.txt") as file: 
	text = file.read()
	easy_words_gen = jieba.cut(text)

for word in words_gen:
    words[word] = words.get(word, 0) + 1

for word in easy_words_gen:
	if word in words:
		del words[word]

top_words = sorted(words.items(), key=itemgetter(1), reverse=True)

for word, frequency in top_words:
	print ("%d\t\t%s" % (frequency, word.encode(default_encoding)))

