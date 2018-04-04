# sort list of words from longest to shortest
def sort_by_length(words):
	t=list()
	for word in words:
		t.append((len(word),word))	#using tuples to sort by DSU
	t.sort(reverse=True)
	res=list()
	for length,word in t:
		res.append(word)
	return res

print 'Enter list of words.Type #done to stop'
t=list()

while True:
	inp=raw_input('>')
	if inp=='#done':
		break
	tmp=inp.split()		#handling sentences entered
	for word in tmp:
		t.append(word)

ans=sort_by_length(t)
print ans
