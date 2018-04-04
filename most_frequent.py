# print letters of string in decreasing order of frequency
import string
s=raw_input('Enter a string: ')
s=s.translate(None,string.punctuation)
d=dict()

for c in s:
	if c not in d:		#creating a dictionary
		d[c]=1
	else:
		d[c]+=1

lst=list()
for key,val in d.items():
	lst.append((val,key))	#for sorting w.r.t values

lst.sort(reverse=True)

for freq,letters in lst:
	print letters
