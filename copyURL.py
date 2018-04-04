# copy binary files to local drive
import os
import urllib

urlstr=raw_input('Enter a url: ').strip()
img=urllib.urlopen(urlstr)

# geting the file name from last word of url
words=urlstr.split('/')
fname=words[-1]

# avoiding file overwrite
if os.path.exists(fname):
	if raw_input('Replace '+fname+' (Y/n)?') !='Y':
		print 'Data not copied'
		exit()
	print 'Replacing', fname

# fetching and writing file from url
fhand=open(fname,'w')
size=0
while True:
	info=img.read(100000)
	if len(info)<1:
		break
	size=size+len(info)
	fhand.write(info)

print size,'characters copied to',fname
fhand.close()
