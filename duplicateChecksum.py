# find duplicate files using hashing/checksum algo
import os
import hashlib

count=0
tmp=dict()
for (dirname,dirs,files) in os.walk('.'):
    for filename in files:
        thefile=os.path.join(dirname,filename)
        size=os.path.getsize(thefile)
        fhand=open(thefile,'r')
        data=fhand.read()
        fhand.close()
        checksum=hashlib.md5(data).hexdigest()
        val=tmp.get(checksum,0)
        if val==0:
            tmp[checksum]=thefile
        else:
            count=count+1
            print tmp[checksum],thefile
print 'Total duplicates:',count