#!/usr/bin/python
#filename:cpick
import cPickle as p
filename='shoplist.data'
shoplist='''\
hahahahaha
hehehehehe
xixixixixi
'''
f=file('shoplist.data','w')
p.dump(shoplist,f)
f.close()

del shoplist

f=file('shoplist.data')
storedlist=p.load(f)
print storedlist


