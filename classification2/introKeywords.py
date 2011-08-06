#!/usr/bin/python
import nltk
from sets import Set
import os

def ascii(c, mode):
	if (mode == 0 and '0' <= c and c <= '9') or ('A' <= c and c <= 'Z') or ('a' <= c and c <= 'z'):
		return 1
	return 0

def ascifi(x, mode):
	y = ""
	for c in x:
		if ascii(c, mode):
			y += c
	return y

def getIntroKeywords(page):
	f = open(page)
	lines = f.readlines()	# First line is empty, read the second line
	text = lines[1] + " " + lines[2] + " " + lines[3]
	tokens = nltk.word_tokenize(text)
	filter = []
	for t in tokens:
		if len(ascifi(t,1)) > 4:
			filter.append(ascifi(t,1))
	set1 = Set(filter)
	set2 = Set(stopWords)
	set3 = Set(commonWords)
	return (set1.difference(set2)).difference(set3)

def getVector(list1, set1, dest):
	list2 = []
	for x in list1:
		if x in set1:list2.append(1)
		else: list2.append(0)
	f = open(dest, 'w')
	f.write(str(list2))
	f.close()
	return list2

f = open("common/stopwords.txt")
stopWords = f.readline().split(",")
f.close()
f = open("common/commonWords.txt")
commonWords = f.readline().split(",")
f.close()								# Get the stopwords

# Get the keywords in the main file
while 1:
	try:
		name = raw_input()
		print name
		if 1: #not os.path.exists('./'+name+'IntroKey.txt'):
			mySet = getIntroKeywords(name+"Body.txt")
			st = ""
			for x in mySet:	st += x + "\n"
			f = open(name+'IntroKey.txt', 'w')
			f.write(st)
			f.close()
	except EOFError:break



