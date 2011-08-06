#!/usr/bin/python
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

out = ""
while 1:
	try:
		article = raw_input()
		f = open("./"+article+".html")
		articleBody = [x[0:-1] for x in f.readlines()]
		for i in range(len(articleBody)):
			try:
				if (articleBody[i].count('<div id="catlinks" class="catlinks">') > 0):
					string = clean(articleBody[i].split("<div id=\"mw-hidden-catlinks\"")[0].strip())
					out += article + " : " + string.replace("Categories: ", "").replace("|", ",") + "\n"
			except Exception as e:
				print type(e), e
				continue
	except EOFError:
		break
f = open("./categories/main",'w')
f.write(out)
f.close()
