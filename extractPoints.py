# extract floating points from any line of a given file using regex
import re
inp=raw_input('Enter file name:')
try:
	fhand=open(inp)
except:
	print 'File cannot be opened,',inp
	exit()
for line in fhand:
	line=line.strip()
	#if re.search('^X\S*: [0-9.]+',line):	# print lines starting with X
	#x=re.findall('^Details:.*rev=([0-9.]+)',line)	#extracting revision numbers
	x=re.findall('^X\S*: ([0-9.]+)',line)	# extracing only floating points
	if len(x)>0:
		print x

