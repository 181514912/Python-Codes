# request and display (first 3000 chars) document from web server using HTTP protocol
from __future__ import print_function
import urllib

urlstr=raw_input('Enter url: ')
try:
	fhand=urllib.urlopen(urlstr)
except:
	print('Not a valid url')
	exit()

count=0
for line in fhand:
	for ch in line:
		if count<=3000:
			print(ch,end='')
		count+=1

print('Total %d characters were present'%count)
