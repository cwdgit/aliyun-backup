#!/usr/bin/python
shoplist=['apple','mango','carrot','banana']
time=len(shoplist)
for i in range(1,time):
  print 'Item',i,'is',shoplist[i]
  print shoplist[i:i+2]
name= 'swaroop'
print 'characters 1 to 3 is',name[1:3]
print 'characters 2 to end is',name[2:]
print 'characters 1 to -1 is', name[1:-1]
print 'characters start to end is',name[:]

