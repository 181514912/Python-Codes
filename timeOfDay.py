# count the distribution of the hour of the hour of the day for each of the messages
inp=raw_input('Enter file name: ')

try:
	fhand=open(inp)
except:
	print 'File cannot be opened,',inp
	exit()

d=dict()

for line in fhand:
	words=line.split()
	if len(words)>=6 and words[0]=='From':
		time=words[5].split(':')
		val=d.get(time[0],0)
		d[time[0]]=val+1
'''
# another approach using regex
import re
for line in fhand:
	line=line.strip()
	x=re.findall('^From .* ([0-9][0-9]):',line)
	if len(x)>0:
		val=d.get(x,0)
		d[x]=val+1

'''
lst=d.keys()
lst.sort()
for key in lst:
	print key,d[key]
