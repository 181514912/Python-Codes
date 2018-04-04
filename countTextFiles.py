# count number of txt files in current working directory along with bad files (recognition pattern is file size)
import os
count=0
for (dirname,dirs,files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.txt'):
            count=count+1
            thefile=os.path.join(dirname,filename)
            size=os.path.getsize(thefile)
            #print size,thefile
            if size==1024 or size==1280:
                print 'Bad Files:',thefile
                os.remove(thefile)
                continue
            fhand=open(thefile,'r')
            lines=list()
            for line in fhand:
                lines.append(line)
            fhand.close()
            if len(lines)==5 and lines[2].startswith('Error data !!'):
                print 'Error files:',thefile
                os.remove(thefile)
                continue
print 'Files:',count