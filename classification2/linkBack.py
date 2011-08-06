#!/usr/bin/python
from sets import Set
import string

def jaquardSimilarity(list1, list2):
	set1 = Set(list1)
	set2 = Set(list2)
	union = set1.union(set2)
	return float(len(set2)+len(set1)-len(union))/float(len(union))

while 1:
	try:
		name = raw_input()
		f = open(name+"Links.txt")
		links = [string.lower(x[0:-1].replace("http://en.wikipedia.org/wiki/","")) for x in f.readlines()]
		f.close()
		st = ""
		for i in range(len(links)):
			try:
				fileName = "outputs_"+name+"/temp" + str(i) + "Links.txt"
				f = open(fileName)
				links2 = [string.lower(x[0:-1].replace('/wiki/','')) for x in f.readlines()]
				f.close()
				flag = links2.count(string.lower(name))
				st += links[i] + " "+str(flag) + '\n'
			except Exception as e:
				print e			
				continue
		f = open("./similarity/linkBack/"+name,'w')
		f.write(st)
	except EOFError:
		break
