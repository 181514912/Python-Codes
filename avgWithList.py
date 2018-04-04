# program to compute average using list
nums=list()
while(True):
	inp=raw_input('Enter a number: ')
	if inp=='done':
		break
	try:
		value=float(inp)
		nums.append(value)
	except:
		print 'Not a number'
avg=sum(nums)/len(nums)
print 'Average: ',avg
