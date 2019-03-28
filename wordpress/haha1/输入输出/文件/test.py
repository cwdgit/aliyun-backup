#!/usr/bin/python
test='''\
hahahahahaha
hehehehehehe
heiheiheihei
'''
f=file('test.txt','w')
f.write(test)
f.close()

f=file('test.txt')
while True:
  line=f.readline()
  if len(line) == 0:
     break
  print line,

f.close()
