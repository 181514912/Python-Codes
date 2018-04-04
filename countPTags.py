# extract and count 'p' tags from the retrieved HTML document
from bs4 import *
import urllib

urlstr=raw_input('Enter url - ')
html=urllib.urlopen(urlstr).read()
soup=BeautifulSoup(html)

# retrive all of the paragraph tags
tags=soup('p')
count=0
for tag in tags:
	count+=1

print 'Total %d paragraphs present'%count
