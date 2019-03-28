#!/usr/bin/python
name='swaroop'
if name.startswith('swa'):
   print 'Yes, the string starts with "swa"'
if 'a' in name:
  print 'Yes, it containers the string "a"'
if name.find('war') !=-1:
  print 'Yes, it contains the string "war"'

delimiter='_*_'
mylist=['a','b','c']
print delimiter.join(mylist)

