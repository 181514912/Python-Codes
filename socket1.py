# request and display document from web server using HTTP protocol
from __future__ import print_function
import socket

mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
urlstr=raw_input('Enter url of data to fetch: ')
words=urlstr.split('/')

try:
	mysock.connect((words[2],80))	#making connection to port 80 on the server
except:
	print('Not a valid url')
	exit()

mysock.send('GET '+urlstr+' HTTP/1.0\n\n')
count=0
data=""
todisplay=""
while True:
	temp=mysock.recv(512)	#receive data in 512 char chunk
	if (len(temp)<1):
		break
	data=data+temp
for ch in data:
	if count <=3000:
		print(ch,end="")
	count+=1

print ('\nTotal characters in docs is '+str(count))

mysock.close()
