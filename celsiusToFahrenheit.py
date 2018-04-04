temp=raw_input('enter celsius temperature: ')
try:
	cels=float(temp)
	fahren=cels*1.8+32
	print 'Fahrenheit temperature: '+str(fahren)
except:
	print 'Please enter a number'
