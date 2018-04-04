# who sent the message using mail box data
inp=raw_input('Enter file name: ')
try:
	fhand=open(inp)
	count=0
	for line in fhand:
		words=line.split()
		if len(words)>=2 and words[0]=='From':
			count=count+1
			print words[1]
	print 'There were %d lines in the file with From as the first word'%count
except:
	print 'No such file found'
