#!/usr/bin/python
import os
import time
source=['/home/swaroop/byte','/home/swaroop/bin']
target_dir='/mnt/backup'
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = "zip -qr %s %s"%(target,' '.join(source))

if os.system(zip_command) == 0:
  print 'successful backup to', target
else:
  print 'backup failed'
