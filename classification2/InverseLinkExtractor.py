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
inLink1 = "http://en.wikipedia.org/w/index.php?title=Special:WhatLinksHere/"
inLink2 = "&limit=10000"
import os

# Removes all newline characters and replaces with spaces
def removeNewLines(in_text):
	return in_text.replace('\n', ' ')

# Downloads a link into the destination
def download(link, dest):
	# print link
	commands.getoutput('wget "' + link + '" -O "' + dest+'"')

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
		name = raw_input()
		inLink = inLink1+name+inLink2
		#download(inLink, "./"+name+"2.html")
		f = open("./"+name+"2.html")
		articleBody = [x[0:-1] for x in f.readlines()]
		st = ""
		for i in range(len(articleBody)):
			if(articleBody[i].strip()[0:4]=="<li>"):
				add = clean(articleBody[i]).strip("(links)").strip() + "\n"
				if add.count("Talk:") > 0: continue
				add = add.replace(" ","_")
				st += add
		f = open("./"+name+"Links2.txt", 'w')
		f.write(st)
		f.close()

		f = open(name+output2)
		links = f.readlines()
		count = 0
		for x in links:
			path1 = "./outputs_"+name+"/temp"+str(count)+"Links2.txt"
			if os.path.exists(path1) and os.path.getsize(path1) > 0: continue
			inLink = inLink1+x.strip("http://en.wikipedia.org/wiki/").strip("\n")+inLink2
			#print inLink
			download(inLink, str("./temp2.html"))
			f = open("./temp2.html")
			articleBody = [x[0:-1] for x in f.readlines()]
			st = ""
			for i in range(len(articleBody)):
				try:
					if(articleBody[i].strip()[0:4]=="<li>"):
						add = clean(articleBody[i]).strip("(links)").strip() + "\n"
						if add.count("Talk:") > 0: continue
						add = add.replace(" ","_")
						st += add
				except Exception as e:
					print type(e), e
					continue
			f = open("./outputs_"+name+"/temp"+str(count)+"Links2.txt", 'w')
			f.write(st)
			f.close()
			print count
			count += 1
	except(EOFError):
		break
	except Exception as e:
		print type(e), e

