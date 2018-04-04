# count the domain name where the message was from
fname=raw_input('Enter file name: ')
try:
	fhand=open(fname)
except:
	print 'File cannot be opened,',fname
	exit()

# creating dictionary
d=dict()
for line in fhand:
	words=line.split()
	if len(words)>=2 and words[0]=='From':
		s=words[1]
		atpos=s.find('@')
		domain=s[atpos+1:].strip()	# finding domain from mail address
		val=d.get(domain,0)
		d[domain]=val+1		# using dictionary as counter

print d
