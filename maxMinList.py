# find max and min of numbers entered using list
nums=list()
while(True):
	inp=raw_input('Enter a number: ')
	if inp=='done':
		break
	try:
		num=float(inp)
		nums.append(num)
	except:
		print 'Not a number'
maxi=max(nums)
mini=min(nums)
print 'Maximum is: ',maxi
print 'Minimum is: ',mini
