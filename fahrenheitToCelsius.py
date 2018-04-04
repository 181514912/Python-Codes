tmp=raw_input('Enter a Fahrenheit temperature: ')
try:
	fahr=float(tmp)
	cels=(fahr-32.0)*5.0/9.0
	print 'Celsius temperature: '+str(cels)
except:
	print 'Please enter a number'
