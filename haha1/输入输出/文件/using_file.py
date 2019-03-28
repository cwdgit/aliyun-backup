#!/usr/bin/python
#filename: using_file.py
poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
   use Python!
'''

#f=file('poem.txt','w') #open for 'w'riting
#f.write(poem)
#f.close()
a=0
f=file('poem.txt')
while True:
  line=f.readline()
  if len(line)==0:
     break
  a=a+1
  print line,
print a
f.close

