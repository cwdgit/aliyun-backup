number=23
running=True
while running:
  guess=int(raw_input('Enter an number  '))
  if guess == number:
    print 'Contratulations,you guessed it.'
    running=False
  elif guess < number:
    print 'No, it is high'
  else:
    print 'No, it is low'

else:
  print 'The while loop is over.'

print 'Done'
