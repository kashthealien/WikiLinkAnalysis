#!/usr/bin/python
while 1:
	try:
		name = raw_input()
		f = open(name+"Links.txt")
		links = [x[0:-1].replace("http://en.wikipedia.org","") for x in f.readlines()]
		f.close()
		st = ""
		for i in range(len(links)):
			try:
				fileName = "outputs_"+name+"/temp" + str(i) + "Links.txt"
				f = open(fileName)
				links2 = [x[0:-1] for x in f.readlines()]
				fileName2 = "outputs_"+name+"/temp" + str(i) + "Links2.txt"
				f2 = open(fileName2)
				links3 = [x[0:-1] for x in f2.readlines()]

				fileName2 = "outputs_"+name+"/temp" + str(i) + "Body.txt"
				f = open(fileName2)
				lent = len(f.read())
				st += links[i]+ " " +str(len(links2)) + " " + str(len(links3)) +" " +str(lent) +"\n"
				f.close()
			except:
				continue
			print i
		f = open("./similarity/lengths/"+name,'w')
		f.write(st)
	except EOFError:
		break
