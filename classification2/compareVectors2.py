#!/usr/bin/python
def jaquardSimilarity(list1, list2):
	inter = 0
	numL1 = 0
	numL2 = 0
	for x in range(len(list1)):
		inter += list1[x]*list2[x]
		numL1 += list1[x]
		numL2 += list2[x]
	union = numL1 + numL2 - inter
	return float(inter)/float(union)

while 1:
	try:
		name = raw_input()
		fileName = name+"Vec.txt"
		f = open(fileName)
		vec1 = eval(f.read())
		f.close()
		vectors = []
		f = open(name+"Links.txt")
		links = [x[0:-1] for x in f.readlines()]
		st = ""
		f.close()
		for i in range(len(links)):
			try:
				fileName = "outputs_"+name+"/temp" + str(i) + "Vec.txt"
				f = open(fileName)
				vec2 = eval(f.read())
				st += links[i]+ " " +str(jaquardSimilarity(vec1, vec2))+"\n"
				f.close()
			except:
				continue
			print i
		f = open("./similarity/lexical/"+name,'w')
		f.write(st)
	except EOFError:
		break
	except Exception as inst:
		f.write(st)
		print type(inst), inst.args
		continue

