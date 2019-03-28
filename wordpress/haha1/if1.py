#!/usr/bin/python
number=44
guess = int(raw_input('please input a number: '))
if guess == number:
   print 'congratulations, you guessed it.'
elif guess > number:
   print 'your guess is higher.'
else:
   print 'your guess is lower.'

print 'done'
