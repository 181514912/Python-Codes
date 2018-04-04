# demonastrat command line input and processing
import sys
print 'Count:',len(sys.argv)
print 'Type:',type(sys.argv)
for arg in sys.argv:
    print 'Argument:',arg
name=sys.argv[1]
try:
    handle=open(name,'r')
except:
    print 'File cannot be opened',name
    exit()
text=handle.read()
print name,'is',len(text),'bytes'