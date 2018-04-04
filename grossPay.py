tmp1=raw_input('enter hours: ')
try:
	hrs=float(tmp1)
	tmp2=raw_input('enter rate: ')
	rate=float(tmp2)
	extra=0
	if hrs>40:
		extra=(hrs-40)*1.5*rate
		hrs=40
	pay=hrs*rate+extra
	print 'Pay: '+str(pay)
except:
	print 'Error! please enter numeric input'
