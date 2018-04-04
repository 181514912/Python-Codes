# Given a string, count how many times each letter appesrs

#method 1
def histogram1(s):
	d=dict()	#creating dictionaries
	for c in s:
		if c not in d:
			d[c]=1
		else:
			d[c]=d[c]+1
	return d

#method 2
def histogram2(s):
	d=dict()
	for c in s:
		val=d.get(c,0)	#key and default value
		d[c]=val+1
	return d

#funtion call
s=raw_input('Enter a string: ')
d=histogram2(s)
print d
