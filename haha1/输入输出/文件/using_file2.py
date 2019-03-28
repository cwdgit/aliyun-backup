#!/usr/bin/python
#filename:testfile

word='''I am a good man,but i am not a good man \
you are a bad man,but you are a bad man.'''

f=file('word.txt','w')
f.write(word)
f.close()

f=file('word.txt')
while True:
  line=f.readline()
  if len(line) == 0:
     break
  print line,

f.close()
