#!/usr/bin/python
#filename test
word='''\
This is a test word
I don't know what i saying
and i don't know everything.
'''
f=file('test.txt','w')
f.write(word)
f.close()


f=file('test.txt')
while True:
  line=f.readline()
  if len(line) == 0:
     break
  print line,

f.close()
