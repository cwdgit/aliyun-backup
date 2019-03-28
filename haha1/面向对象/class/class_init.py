#!/usr/bin/python
#filename: class_init.py
class Person:
  def __init__(self,name):
     self.name = name
     print '__init__ name is',name
  def sayHi(self):
     print 'Hello, my name is',self.name

p=Person('swaroop')
p.sayHi()
