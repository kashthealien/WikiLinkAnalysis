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

def getKeywords(page):
	f = open(page)
	text = f.read()
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

# BEIGINNING

# CREATE A STOP WORDS LIST
f = open("common/stopwords.txt")
stopWords = f.readline().split(",")
f.close()
f = open("common/commonWords.txt")
commonWords = f.readline().split(",")
f.close()

# Get the keywords in the main file
while 1:
	name = raw_input()
	mySet = getKeywords(name+"Body.txt")
	st = ""
	for x in mySet:	st += x + "\n"
	f = open(name+"Key2.txt", 'w')
	f.write(st)
	f.close()

	f = open(name+"Links.txt")
	MAX = len(f.readlines())
	f.close()

	# Get the keywords in all linked files
	for i in range(MAX):
		try:
			fileName = "temp" + str(i) + "Body.txt"
			myList = getKeywords("outputs_"+name+"/"+fileName)
			if not os.path.exists("outputs_"+name+"/temp"+str(i)+"Key2.txt"):
				st = ""
				for x in myList: st += x + "\n"
				f = open("outputs_"+name+"/temp" + str(i) + "Key2.txt", 'w')
				f.write(st)
				f.close()
			print i					
		except:
			continue
