#!/usr/bin/python
number=23
status=True
while status:
  guess=int(raw_input('enter a number '))
  if guess == number:
    print 'congratulations, you guessed it.'
    status=False
  elif  guess > number:
    print 'the number is higher.'
  else:
    print 'the number is lower.'

else:
  print 'the while loop is over.'

print 'Done'
