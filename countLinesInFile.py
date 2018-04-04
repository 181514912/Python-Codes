fname=raw_input('Enter file name: ')
#adding Easter Eggs
if fname=='na na boo boo':
	print "NA NA BOO BOO TO YOU - You have been punk'd!"
	exit()
#Easter Eggs ends
try:
	fhand=open(fname)
except:
	print 'File cannot be opened: ',fname
	exit()
count=0
for line in fhand:
	if line.startswith('Subject:'):
		count=count+1
print 'There were ',count,' subject lines in ',fname
