print "Enter numbers. To stop enter 'done'"
total=0.0
count=0
while True:
	temp=raw_input('>')
	if temp=='done':
		break
	try:
		num=float(temp)
		count=count+1
		total=total+num
	except:
		print 'Invalid input'
avg=total/count
print 'Total: ',total
print 'Count: ',count
print 'Average: ',avg
