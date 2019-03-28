#!/usr/bin/python
#filename: backup_ver1.py
import os
import time
#1.The files and directories to be backed up are specified in a list
source = ['/home/swaroop/byte','/home/swaroop/bin']
#2.The backup must be stored in a main backup directory
target_dir = '/mnt/backup/' #remeber to change this to what you will be using
#3.The files are backed up into a zip file.
#4.The name of the zip archive is the current date and time
target= target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
#5.we use the zip command (in Unix/Linux) to put the files in a zip file
zip_command = "zip -qr '%s' %s" %(target, ' '.join(source))

if os.system(zip_command) == 0:
   print 'successful backup to',target
else:
   print 'backup failed'

