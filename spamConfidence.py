fname=raw_input('Enter file name: ')
try:
	fhand=open(fname)
except:
	print 'Cannot open file: ',fname
	exit()
count=0
tot=0
for line in fhand:
	if line.startswith('X-DSPAM-Confidence:'):
		count=count+1
		cpos=line.find(':')
		tmp=line[cpos+1:]
		num=float(tmp.strip())
		tot=tot+num
avg=tot/count
print 'Average spam confidence: ',avg
