# print ten most common words along with there occurences from a text
import string
inp=raw_input('Enter file name: ')

try:
	fhand=open(inp)
except:
	print 'File cannot be opened,',inp
	exit()

counts=dict()
for line in fhand:
	line=line.translate(None,string.punctuation)	#removing special chars
	line=line.lower()
	words=line.split()
	for word in words:		#inserting words in dictionary
		if word not in counts:
			counts[word]=1
		else:
			counts[word] +=1

#sorting the dictionary by value
lst=list()
for key,val in counts.items():
	lst.append((val,key))

lst.sort(reverse=True)

for key,val in lst[:10]:	#printing ten most common words
	print key,val

