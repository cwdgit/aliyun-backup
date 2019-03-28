#!/usr/bin/python
#'ab' is short for 'a' address 'b'ook
ab = {'swaroop':'swaroopch@byteofpython.info',
      'Larry': 'larry@wall.org',
      'Matsumoto' : 'matz@ruby-lang.org',
      'Spammer': 'spammer@hotmail.com'

}
print "Swaroop's address is %s" %ab['swaroop']
ab['guido']='guido@python.org'
for name,address in ab.items():
  print 'contact %s at %s' %(name,address)
if 'guido' in ab:
  print "\nguido's address is %s" %ab['guido']
