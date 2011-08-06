#Imports
import httplib2
from BeautifulSoup import BeautifulSoup
import commands
import time
import os

#declarations
catRoot = "http://en.wikipedia.org/wiki/Category:"
MAX_DEPTH = 100
done = ['Algorithms', 'Artificial_intelligence', 'Computational_science','Computer_architecture',\
		'Concurrency','Data_structures','Database_theory','Computer_graphics',\
		'Human-based_computation', 'Computer_science_literature','Operating_systems',\
		'Computer_scientists', 'Computer_security', 'Software_engineering',\
		'Computer_science_organizations','Programming_language_theory','Programming_languages'\
		'Information_theory']
ignore = ['NUTS', 'Light','Archaeological_corpora','Rockets_and_missiles','Espionage', 'Prisons',\
		'Classification_systems','Strategic_management','Tactics','Taxonomy','Cartography',\
		'Infographics', 'Graphic_design', 'Free_wiki_software', 'Crowd_psychology', 'Free_websites',\
		'Digital_technology','Lexical_semantics','Diagrams','Semantics']
# Removes all newline characters and replaces with spaces
def removeNewLines(in_text):
    return in_text.replace('\n', ' ')

# Downloads a link into the destination
def download(link, dest):
    # print link
    if not os.path.exists(dest):
	    commands.getoutput('wget "' + link + '" -O "' + dest+ '"')
    
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

# Gets bullets
def getBullets(content):
    mainSoup = BeautifulSoup(contents)
    
# Gets empty bullets
def getAllBullets(content):
    mainSoup = BeautifulSoup(str(content))
    subcategories = mainSoup.findAll('div',attrs={"class" : "CategoryTreeItem"})

    empty = []
    full = []
            
    for x in subcategories:
    	subSoup = BeautifulSoup(str(x))
    	link = str(subSoup.findAll('a')[0])
        if (str(x)).count("CategoryTreeEmptyBullet") > 0:
            empty.append(clean(link).replace(" ","_"))
        elif (str(x)).count("CategoryTreeBullet") > 0:
            full.append(clean(link).replace(" ","_"))

    return((empty,full))

def printTree(catName, count):
    if count == MAX_DEPTH: return
    download(catRoot+catName, "Category:"+catName+".html")
    f = open("Category:"+catName+".html")
    content = f.readlines()
    (emptyBullets,fullBullets) = getAllBullets(content)
    f.close()

    for x in emptyBullets:
        for i in range(count): print "  ",
        print x

    for x in fullBullets:
        for i in range(count): print "  ",
        print x
       	if x in done:
       		print "Done... "+x
       		continue
       	elif x in ignore:
            print "Ignored... " + x
            continue
        done.append(x)
        try:
            printTree(x, count + 1)        
        except:
        	print "ERROR: " + x

name = "Computer_science"
printTree(name, 0)
