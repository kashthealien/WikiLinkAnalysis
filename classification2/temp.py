#!/usr/bin/python
from sets import Set

def jaquardSimilarity(list1, list2):
	set1 = Set(list1)
	set2 = Set(list2)
	union = set1.union(set2)
	return float(len(set2)+len(set1)-len(union))/float(len(union))

fileName = "/home/kashyap/projects/BTP/classification2/GoldKey.txt"
f = open(fileName)
vec1 = [x[0:-1] for x in f.readlines()]

fileName = "/home/kashyap/projects/BTP/classification2/outputs_Gold/temp0Key.txt"
f = open(fileName)
vec2 = [x[0:-1] for x in f.readlines()]

fileName = "/home/kashyap/projects/BTP/classification2/outputs_Gold/temp8Key.txt"
f = open(fileName)
vec3 = [x[0:-1] for x in f.readlines()]

print Set(vec1).intersection(Set(vec2)), len(Set(vec1).intersection(Set(vec3)))
print len(vec1), len(vec3)
