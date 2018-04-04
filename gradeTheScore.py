def computegrade(score):
	if not(score>=0.0 and score<=1.0) :
		return 'Error! Bad Score'
	else:	
		if score>=0.9:
			return 'A'
		elif score>=0.8:
			return 'B'
		elif score>=0.7:
			return 'C'
		elif score>=0.6:
			return 'D'
		else:
			return 'F'

tmp=raw_input('Enter a score between 0.0 and 1.0: ')
try:
	score=float(tmp)
	grade=computegrade(score)
	print grade
except:
	print 'Error! Bad Score'
