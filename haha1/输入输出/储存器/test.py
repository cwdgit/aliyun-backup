#!/usr/bin/python
# filename: cunchu
import cPickle as p

filename='shoplist.data'
data=['apple','mango','banana']
f=file(filename,'w')
p.dump(data,f)
f.close()

f=file(filename)
test=p.load(f)
print test

