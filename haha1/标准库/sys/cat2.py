#!/usr/bin/python
#filename:cat2.py
import sys

def readfile(filename):
  f=file(filename)
  while True:
    line=f.readline()
    if len(line)==0:
       break
    print line,
  f.close()

if len(sys.argv) < 2:
   print 'no action specifed'
   sys.exist()
if sys.argv[1].startswith('--'):
   option=sys.argv[1][2:]
   print option
   if option == 'version':
      print 'Version 1.2'
   elif option == 'help':
      print 'you can add -- version get the version \
                     add -- help get the help'
   else:
     print 'unknown the option'
     sys.exit()
else:
  for filename in sys.argv[1:]:
    print filename
    readfile(filename)
  
   
