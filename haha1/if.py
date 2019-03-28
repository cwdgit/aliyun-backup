#!/usr/bin/python
number = 23
guess = int(raw_input('enter an integer : '))
if guess == number:
    print 'Congratulations you guessed it.'
elif guess > number:
    print 'No, it is a little higher'
else:
    print 'no, it is a little lower'

print 'done'
