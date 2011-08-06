#!/usr/bin/python
import string
from sets import Set
NUM = 7
PATH_START = "./similarity/"
l = ["links/", "lexical2/", "lengths/", "cats1/", "introLexical/", "colinks/", "linkBack/"]
pos = [3, 4, 5, 8, 9, 10, 11]
def add(dictionary, n, item, li):
	if item in dictionary:
		if(len(dictionary[item]) == n-1):
			return
		else:
			dictionary[item].extend(li)
	else: dictionary[item] = li

while 1:
	try:
		article = raw_input()
		print article
		f = []
		lines = []
		linkMap = {}
		# List out the files that should be read and read them and append to lines
		for i in range(NUM):
			f.append(open(PATH_START+l[i]+article))
			lines.append(Set([x[0:-1] for x in f[i].readlines()]))
		# Print the header
		st = "Link " + "outLinkSimilarity " + "inLinkSimilarity " + "lexicalSimilarity " + "numOutLinks " +\
		 "numInLinks " + "Length " + "CategorySimilarity " + "introSimilarity " +\
		 "linkCooccurance " + "backLinks " + "\n"
		# For each attribute, for each entry, add values to the dictionary of the link to get {link:value}
		for i in range(NUM):
			for x in lines[i]:
				a = x.split()
				a[0] = a[0].replace('http://en.wikipedia.org/wiki/','').replace('/wiki/','')
				add(linkMap, pos[i], string.lower(a[0]), a[1:])
		# For each link, print if all values are available
		for a in linkMap.keys():
			if len(linkMap[a]) == 10:
				st += a + " , " + str(map(float,linkMap[a]))[1:-1] +"\n"
			else:
				print 'Error', a + " , " + str(map(float,linkMap[a]))[1:-1]
		f = open('./similarity/'+article+"New",'w')
		f.write(st)		
	except EOFError:
		break

