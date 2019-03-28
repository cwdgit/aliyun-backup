#!/usr/bin/python
#(class and object)'s var
class Person:
  '''Represents a person.'''
  population = 0
  print 'test'
  def __init__(self,name):
    '''Initializes the person's data.'''
    self.name = name
    print '(Initializing %s)' %self.name
    Person.population +=1
   
  def __del__(self):
     '''I am dying.'''
     print '%s says bye.' %self.name
     Person.population -=1
     if Person.population ==0:
        print 'I am the last one.' 
     else:
        print 'There are still %d people left.' %Person.population
  
  def sayHi(self):
     '''Greeting by the person.
     really, that's all it does.'''
     print 'Hi, my name is %s.' %self.name
  
  def howMany(self):
     '''prints the current population.'''
     if Person.population == 1:
        print 'I am the only person here.'
     else:
        print 'we have %d persons here.' %Person.population

swaroop = Person('swaroop')
swaroop.sayHi()
swaroop.howMany()

cwd = Person('cwd')
cwd.sayHi()
cwd.howMany()

swaroop.sayHi()
swaroop.howMany()

