# sort and print words of a file in alphabetical order.
ipn=raw_input('Enter file name: ')
try:
	fhand=open(ipn)
	ans=list()
	for line in fhand:
		words=line.split()
		for word in words:
			if not word in ans:
				ans.append(word)
	ans.sort()
	print ans
		
except:
	print 'No such file found'
