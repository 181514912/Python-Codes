# count mail messages by which day of the week it was commited
inp=raw_input('Enter file name: ')
try:
	fhand=open(inp)
except:
	print 'File cannot be opened,',inp
	exit()

d=dict()
for line in fhand:
	words=line.split()
	if len(words)>=3 and words[0]=='From':
		val=d.get(words[2],0)
		d[words[2]]=val+1

print d
