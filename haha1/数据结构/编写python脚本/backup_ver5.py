#!/usr/bin/python
#filename:backup4
import os
import time
source = ['/home/swaroop/byte','/home/swaroop/bin']
target_dir='/mnt/backup'
today=target_dir+time.strftime('%Y%m%d')
now=time.strftime('%H%M%S')
'''
if not os.path.exists(today):
   os.mkdir(today)
   print 'successfully created directory',today
target = today + os.sep + now + '.zip'
zip_command='zip -qr %s %s' %(target, ' '.join(source)) 
if os.system(zip_command) == 0:
   print 'successful backup to',target
else:
   print 'back failed'
'''
comment = raw_input('Enter a comment -->')
if len(comment) == 0:
   target = today + os.sep + now + '.zip'
else:  
   target = today + os.sep + '_' + comment.replace(' ','_') + '.zip'

if not os.path.exists(today):
   os.mkdir(today)
   print 'successfully created directory',today

zip_command='zip -qr %s %s' %(target,' '.join(source))

if os.system(zip_command) == 0:
   print 'successful backup to', target
else:
   print 'backup failed'
