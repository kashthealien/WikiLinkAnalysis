#!/usr/bin/python
#Imports
import httplib2
from BeautifulSoup import BeautifulSoup
import commands
import time

#declarations
fileName = ".html"
output = "Body.txt"
output2 = "Links.txt"
import os

# Removes all newline characters and replaces with spaces
def removeNewLines(in_text):
	return in_text.replace('\n', ' ')

# Downloads a link into the destination
def download(link, dest):
	# print link
	commands.getoutput('wget "' + link + '" -O ' + dest)
	
def ensureDir(f):
	if not os.path.exists(f):
		os.makedirs(f)

# Cleans a text by removing tags
def clean(in_text):
	s_list = list(in_text)
	i,j = 0,0
	while i < len(s_list):
		# iterate until a left-angle bracket is found
		if s_list[i] == '<':
			if s_list[i+1] == 'b' and s_list[i+2] == 'r' and s_list[i+3] == '>':
				i=i+1
				print hello
				continue				
			while s_list[i] != '>':
				# pop everything from the the left-angle bracket until the right-angle bracket
				s_list.pop(i)
			# pops the right-angle bracket, too
			s_list.pop(i)

		elif s_list[i] == '\n':
			s_list.pop(i)
		else:
			i=i+1
			
	# convert the list back into text
	join_char=''
	return (join_char.join(s_list))#.replace("<br>","\n")

# Writes the body to $product+Body.txt file
def getBody(product, dest):
	fil = "./"+product + fileName
	if not os.path.exists(fil):
		print "No file " + fil
		return
	myFile = open(fil)
	text = myFile.read().replace('\n',' ')
	mainSoup = BeautifulSoup(text)
	body = mainSoup.findAll('p')
	outStr = ""
	for x in body:
		outStr += clean(str(x)) + "\n"
	f = open(dest+output, 'w')
	f.write(outStr)
	f.close()

# Writes all links to $product+Links.txt file
def getLinks(product, dest):
	# Get body
	fil = product + fileName
	if not os.path.exists(fil):
		print "No file " + fil
		return
	myFile = open(fil)
	mainSoup = BeautifulSoup(myFile)
	body = mainSoup.findAll('p')
	#Get links
	bodySoup = BeautifulSoup(str(body))
	links = bodySoup.findAll('a')
	outStr = ""
	for x in links:
		st = str(x).split("href=\"")[1].split("\"")[0] + "\n"
		st = st.replace("%27","'").replace("%28","(").replace("%29",")")
		if st.count("%")>0: continue				# Ignore wierd links for now, get back later
		if st.count("?")>0: continue				# Ignore wierd links for now <permanent>
		if st[0] == "#":continue					# Ignore in links
		outStr += st

	f = open(dest+output2, 'w')
	f.write(outStr)
	f.close()

while 1:
	try:
		name = raw_input()
		print name
		getBody(name,name)
		print "got body"
		getLinks(name,name)
		print "got links"
		"""
		f = open(name+output2)
		links = f.readlines()
		count = 0
		directory = "./outputs_"+name

		ensureDir(directory)
		for x in links:
			fileName2 = directory+"/temp"+str(count)+output
			if not os.path.exists(fileName2):
				try:
					download(x[0:-1], str("./temp.html"));
					getBody("temp",directory+"/"+"temp"+str(count))
					getLinks("temp",directory+"/"+"temp"+str(count))
					print "yeah", count
				except:
					"nope ", count
			count += 1
		# print count		
		"""
	except(EOFError):
		break

