#!/usr/bin/python
number=23
running=True
while running:
  guess=int(raw_input('Enter an number '))
  if guess == number:
     print 'congratulations, you guessed it.'
     running = False
  elif guess < number:
     print 'No, it is lower'
  else:
     print 'No, it is higher'

else:
  print 'The while loop is over.'
