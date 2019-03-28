#!/usr/bin/python
#filename: test1.py
import cPickle as p
filename='shoplist.data'
fruit=['apple','mango','lemon']

f=file(filename,'w')
p.dump(fruit,f)
f.close()

f=file(filename)
test=p.load(f)
print test
f.close()
