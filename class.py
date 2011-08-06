#!/usr/bin/python
import string
di = {}			#Category dictionary

# Read in the categories
f = open('./data.csv')
lines = [x[0:-1] for x in f.readlines()]
f.close()
for line in lines:
	attrs = line.split(",")
	link = attrs[0].strip().strip('/wiki/')
	category = attrs[-1].strip()
	di[string.lower(link)] = category;

f = open('./classification2/input')
lines = [x[0:-1] for x in f.readlines()]
f.close

st = 'Link, outLinkSimilarity, inLinkSimilarity, lexicalSimilarity, numOutLinks, numInLinks, Length, CategorySimilarity, introSimilarity, linkCooccurance, backLinks, Category \n'
st2= 'Link, outLinkSimilarity, inLinkSimilarity, lexicalSimilarity, numOutLinks, numInLinks, Length, 	CategorySimilarity, introSimilarity, linkCooccurance, backLinks, Category \n'
for line in lines:
	f = open('./classification2/similarity/'+line+"New")
	attrs = [x[0:-1] for x in f.readlines()]
	for link in attrs:
		if string.lower(link.split(',')[0].strip()) in di:
			st += link + ',' + di[link.split(',')[0].strip()] + '\n'
			st2+= link + ',' + di[link.split(',')[0].strip()] + '\n'
		else:
			st2+= link+ '\n'
f = open('./data2.csv','w')
f.write(st)
f.close
f = open('./data3.csv','w')
f.write(st2)
f.close
