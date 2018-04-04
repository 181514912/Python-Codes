def count(stmt,ch):
	count=0
	for letter in stmt:
		if letter==ch:
			count=count+1
	return count
s=raw_input('Enter a string: ')
l=raw_input('Enter a char to count: ')
if len(l)!=1:
	print 'Not a letter !!'
else:
	ans=count(s,l)
	print ans
