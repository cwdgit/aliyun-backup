#!/usr/bin/python
#filename: wenjian1
word='''\
111111111
222222222
333333333
444444444
555555555
666666666
777777777
'''
f=file('test.txt','w')
f.write(word)
f.close()

f=file('test.txt')
while True:
  line=f.readline()
  if len(line)==0:
     break
  print line,

f.close()

