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
	myFile = open(product+fileName)
	mainSoup = BeautifulSoup(myFile)
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
	myFile = open(product+fileName)
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
		out = ""
		count = 0
		article = raw_input()
		f = open(article+output2)
		links = [x[0:-1] for x in f.readlines()]
		if os.path.exists("./categories/"+article+"Categories.txt"): continue
		for x in links:
			print count
			count += 1

			out += x + ' : '
			download(x, "./temp3.html");
			f = open("./temp3.html")
			articleBody = [x[0:-1] for x in f.readlines()]
			for i in range(len(articleBody)):
				try:
					if (articleBody[i].count("<div id='catlinks' class='catlinks'>") > 0):
						string = clean(articleBody[i].split("<div id=\"mw-hidden-catlinks\"")[0].strip())
						out += string.replace("Categories: ", "").replace("|", ",") + "\n"
				except:
					continue
		f = open("./categories/"+article +"Categories.txt",'w')
		f.write(out)
		f.close()
	except(EOFError):
		break
