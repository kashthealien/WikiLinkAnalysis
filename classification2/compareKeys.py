#!/usr/bin/python
from sets import Set
import os

def jaquardSimilarity(list1, list2):
	set1 = Set(list1)
	set2 = Set(list2)
	union = set1.union(set2)
	return float(len(set2)+len(set1)-len(union))/float(len(union))

while 1:
	try:
		name = raw_input()
		fileName = name+"Key2.txt"
		f = open(fileName)
		vec1 = [x[0:-1] for x in f.readlines()]
		f.close()
		vectors = []
		f = open(name+"Links.txt")
		links = [x[0:-1] for x in f.readlines()]
		st = ""
		f.close()
		print name
		for i in range(len(links)):
			try:
				fileName = "outputs_"+name+"/temp" + str(i) + "Key2.txt"
				if os.path.exists(fileName):
					f = open(fileName)
					vec2 = [x[0:-1] for x in f.readlines()]
				else:
					vec2 = []
				st += links[i]+ " " +str(jaquardSimilarity(vec1, vec2))+"\n"
				f.close()
			except Exception as e:
				print e
				continue
		f = open("./similarity/lexical2/"+name,'w')
		f.write(st)
	except EOFError:
		break
	except Exception as inst:
		f.write(st)
		print type(inst), inst.args
		continue

