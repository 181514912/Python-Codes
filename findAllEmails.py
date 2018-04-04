# find all emails from a given file using regex
import re
inp=raw_input('Enter file name: ')
try:
	fhand=open(inp)
except:
	print 'File cannot be opened,',inp
	exit()

for line in fhand:
	line=line.strip()
	x=re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]',line)	# \S=non-whitespace char
	if len(x)>0:
		print x

