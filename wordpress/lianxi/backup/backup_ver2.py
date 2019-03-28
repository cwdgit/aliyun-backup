#!/usr/bin/python
import os 
import time
source = ['/home/swaroop/byte','/home/swaroop/bin']
target_dir='/mnt/backup/'
today = target_dir + time.strftime('%Y%m%d')
now=time.strftime('%H%M%S')

if not os.path.exists(today):
  

