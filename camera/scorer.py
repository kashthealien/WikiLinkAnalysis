raw_input();
while 1:
    try:
        line = raw_input()
        a = [Link,Familiar,Tangential,Parallel,Elaborative,Background,ProperNoun,Utility,outLinkSimilarity,\
	    inLinkSimilarity,lexicalSimilarity,numOutLinks,numInLinks,Length,CategorySimilarity,\
	    introSimilarity,linkCooccurance,backLinks ] = line.split(',')
        utility = 0.1529 * float(Familiar=='n') +\
          0.4795 * float(Tangential=='n') +\
          0.2223 * float(Parallel=='y') +\
          1.3181 * float(Elaborative=='y') +\
          0.5037 * float(Background=='y') +\
          0.1591 * float(ProperNoun=='n') +\
          3.4945 * float(outLinkSimilarity) +\
         11.2287 * float(inLinkSimilarity) +\
          0.2169 * float(CategorySimilarity) +\
         -0.9039 * float(linkCooccurance) +\
          0.0881 * float(backLinks) + 0.5545
        if utility > 3.5:
		    print Link
    except EOFError: break
