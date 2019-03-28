#!/usr/bin/python
#filename: finally.py

import time
test='''\
hahahahah
heheheheh
xixixixix
'''
try: 
  f = file('poem.txt','w')
  f.write(test)
  f.close()
  while True:
    line = f.readline()
    if len(line)==0:
       break
    time.sleep(2)
    print line,

finally:
  f = file('poem.txt')
  f.close()
  print 'Cleaning up...closed the file'
