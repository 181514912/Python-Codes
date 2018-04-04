# program to simulate grep in linux. Count the no. of lines matched using the regex
import re
inp=raw_input('Enter file name:')
try:
	fhand=open(inp)
except:
	print 'File cannot be opened,',inp
	exit()
regex=raw_input('Enter a regular expression:')
count=0
for line in fhand:
	line=line.strip()
	if re.search(regex,line):
		count+=1

print inp,'had %d lines that matched'%count,regex
