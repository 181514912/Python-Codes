# find out who had most messages from a mail log
fname=raw_input('Enter file name: ')
try:
	fhand=open(fname)
except:
	print 'File cannot be opened,',fname
	exit()

d=dict()	#creating dictionary
for line in fhand:
	words=line.split()
	if len(words)>=2 and words[0]=='From':
		val=d.get(words[1],0)
		d[words[1]]=val+1

maxi=None
whois=None

#finding maximum count
for key in d:
	if maxi is None or d[key]>maxi:
		maxi=d[key]
		whois=key

print whois,maxi
