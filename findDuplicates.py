# find and print duplicate files i.e. having same size
import os
tmp=dict()
for (dirname,dirs,files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.txt'):
            thefile=os.path.join(dirname,filename)
            size=os.path.getsize(thefile)
            val=tmp.get(size,0)
            if val==0:
                tmp[size]=thefile
            else:
                tmp[size]=(tmp[size],thefile)
                print tmp[size]