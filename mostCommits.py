# print the person who has the most commits in mail logs
inp=raw_input('Enter file name: ')

try:
	fhand=open(inp)
except:
	print 'File cannot be opened,',inp
	exit()

d=dict()
for line in fhand:
	words=line.split()
	if len(words)>=2 and words[0]=='From':	#creating dictionary counter
		val=d.get(words[1],0)
		d[words[1]]=val+1

lst=list()
for key,val in d.items():
	lst.append((val,key))	#for sorting based on value

lst.sort(reverse=True)
count,mail=lst[0]
print mail,count
