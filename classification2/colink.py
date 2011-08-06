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
		links = [x[0:-1].replace("http://en.wikipedia.org/wiki/","") for x in f.readlines()]
		f.close()
		st = ""
		li = [0]*len(links)
		numInLinks = [0]*len(links)
		for i in range(len(links)):
			print i
			fileName = "outputs_"+name+"/temp" + str(i) + "Links.txt"
			try:
				f = open(fileName)
				links2 = [string.lower(x[0:-1].replace('/wiki/','')) for x in f.readlines()]
				f.close()
			except:
				links2 = []
			flag = links2.count(string.lower(name))
			for j in range(len(links)):
				count2 = links2.count(string.lower(links[j]))
				li[j] += flag*count2
			numInLinks[i] = len(open("outputs_"+name+"/temp" + str(i) + "Links2.txt").readlines())
		for i in range(len(links)):			
			if not numInLinks[i] == 0:
				st += links[i]+" "+str(float(li[i])/float(numInLinks[i])) + "\n"
		f = open("./similarity/colinks/"+name,'w')
		f.write(st)
	except EOFError:
		break
