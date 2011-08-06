#!/usr/bin/python
from sets import Set

def jaquardSimilarity(list1, list2):
	set1 = Set(list1)
	set2 = Set(list2)
	union = set1.union(set2)
	return float(len(set2)+len(set1)-len(union))/float(len(union))

while 1:
	try:
		name = raw_input()
		f = open(name+"Links.txt")
		links = [x[0:-1].replace("http://en.wikipedia.org","") for x in f.readlines()]
		f.close()
		f = open(name+"Links2.txt")
		links3 = [x[0:-1].replace("http://en.wikipedia.org","") for x in f.readlines()]
		f.close()
		st = ""
		for i in range(len(links)):
			try:
				fileName = "outputs_"+name+"/temp" + str(i) + "Links.txt"
				f = open(fileName)
				links2 = [x[0:-1] for x in f.readlines()]
				fileName2 = "outputs_"+name+"/temp" + str(i) + "Links2.txt"
				f2 = open(fileName2)
				links4 = [x[0:-1] for x in f2.readlines()]
				f.close()
				f2.close()
				for j in range(len(links))
       				fileName = "outputs_"+name+"/temp" + str(i) + "Links.txt"
    				f = open(fileName)
    				links2 = [x[0:-1] for x in f.readlines()]
    				fileName2 = "outputs_"+name+"/temp" + str(i) + "Links2.txt"
    				f2 = open(fileName2)
    				links4 = [x[0:-1] for x in f2.readlines()]
    				f.close()
	    			f2.close()
			except Exception as e:
				print e			
				continue
			#print i
		f = open("./similarity/links/"+name,'w')
		f.write(st)
	except EOFError:
		breakwhile 1:
	try:
		name = raw_input()
		f = open(name+"Links.txt")
		links = [x[0:-1].replace("http://en.wikipedia.org","") for x in f.readlines()]
		f.close()
		f = open(name+"Links2.txt")
		links3 = [x[0:-1].replace("http://en.wikipedia.org","") for x in f.readlines()]
		f.close()
		st = ""
		for i in range(len(links)):
			try:
				fileName = "outputs_"+name+"/temp" + str(i) + "Links.txt"
				f = open(fileName)
				links2 = [x[0:-1] for x in f.readlines()]
				fileName2 = "outputs_"+name+"/temp" + str(i) + "Links2.txt"
				f2 = open(fileName2)
				links4 = [x[0:-1] for x in f2.readlines()]
				st += links[i]+ " " +str(jaquardSimilarity(links, links2))+" "+\
								     str(jaquardSimilarity(links3, links4))+"\n"
				f.close()
			except Exception as e:
				print e			
				continue
			#print i
		f = open("./similarity/links/"+name,'w')
		f.write(st)
	except EOFError:
		break
