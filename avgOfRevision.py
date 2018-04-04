# extract new revision and find there average using regex
import re
inp=raw_input('Enter file name:')
try:
	fhand=open(inp)
except:
	print 'File cannot be opened,',inp
	exit()
total=0
count=0
for line in fhand:
	line=line.strip()
	x=re.findall('^New Revision: ([0-9]+)',line)
	if len(x)>0:
		total+=float(x[0])
		count+=1

avg=total/count
print avg
