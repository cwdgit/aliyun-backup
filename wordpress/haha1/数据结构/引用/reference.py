#!/usr/bin/python
print 'simple assignment'
shoplist=['apple','mango','carrot','banana']
print 'shoplist is', shoplist
mylist = shoplist
print 'mylist is', mylist

del shoplist[0]
print 'shoplist is', shoplist
print 'mylist is', mylist

print 'copy by making a full slice'
mylist = shoplist[:]
print mylist
del shoplist[0]
print 'shoplist is', shoplist
print 'mylist is', mylist

