print "Enter numbers. To stop enter 'done'"
maxi=None
mini=None
while True:
	temp=raw_input('>')
	if temp=='done':
		break
	try:
		num=int(temp)
		if maxi is None or num>maxi:
			maxi=num
		if mini is None or num<mini:
			mini=num
	except:
		print 'Invalid input'
print 'Maximum: ',maxi
print 'Minimum: ',mini
