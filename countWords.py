# count occurances of each word using dictionary
import string

inp=raw_input('Enter file name: ')
try:
	fhand=open(inp)
except:
	print 'File cannot be opened: ',inp
	exit()

counts=dict()
for line in fhand:
	line = line.translate(None, string.punctuation)
	# line=line.translate(string.maketrans(' ',' '), string.punctuation) #use for python 2.5 and greater
	line=line.lower()
	words=line.split()
	for word in words:
		if not word in counts:
			counts[word]=1
		else:
			counts[word]+=1
print counts
