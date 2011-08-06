fil = open('Camera.html')
html = fil.read()
scoreFile = open('scores')
scores = [(a.split()[0].replace("(",'%28').replace(")",'%29'), a.split()[1][0:-1]) for a in scoreFile.readlines()]

param = 2
for a in scores:
    if not float(a[1]) > param:
        replaceStr = '<a href="http://en.wikipedia.org' + a[0] +'">'
        #print replaceStr
        html = html.replace(replaceStr,'')
        replaceStr ='<a href="http://en.wikipedia.org' + a[0] +'" class="mw-redirect" title="'\
            +a[0].replace('/wiki/','').replace('_',' ').replace('%28','(').replace('%29',')')+'">'
        #print replaceStr
        html = html.replace(replaceStr,'')
        replaceStr ='<a href="http://en.wikipedia.org' + a[0] +'" title="'\
            +a[0].replace('/wiki/','').replace('_',' ').replace('%28','(').replace('%29',')')+'" class="mw-redirect">'
        print replaceStr
        html = html.replace(replaceStr,'')
        replaceStr = '<a href="http://en.wikipedia.org' + a[0] +'" title="'\
            +a[0].replace('/wiki/','').replace('_',' ').replace('%28','(').replace('%29',')')+'">'
        html = html.replace(replaceStr,'')
print html
