# that takes a list and modifies it, removing the first and last elements, and returns None

def chop(t):
	del t[0] #removing first
	t.pop() #removing last
	return None

# takes a list and returns a new list that contains all but the first and last elements

def middle(t):
	return t[1:len(t)-1]

lets=['a','b','c','d','e']
lets2=lets[:]	#alising
x=chop(lets)
print x
print lets

x=middle(lets2)
print x
print lets2
