#!/usr/bin/python
#init-test

class Person:
  def __init__(self,haha):
     self.haha = haha
  def sayHaha(self):
     print 'This is a test, this is my only can',self.haha

p=Person('cwd')
p.sayHaha()

