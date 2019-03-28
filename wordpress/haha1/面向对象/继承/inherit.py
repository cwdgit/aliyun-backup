#!/usr/bin/python
class SchoolMember:
  '''Represents any school member.'''
  def __init__(self,name,age):
      self.name = name
      self.age = age
      print '(Initialized SchoolMember: %s)' %self.name
  def tell(self):
     '''tell my details.'''
     print 'Name: "%s" Age:"%s"' %(self.name,self.age),
  

class Teacher(SchoolMember):
   '''represents a teacher.'''
  def __init__(self,name,age,salary):
      SchoolMember.__init__(self,name,age)
    self.salary = salary
    print '(Initialized Teacher: %s)' %self.name  
  def tell(self):
    SchoolMember.tell(self)
    print 'Salary: "%d"' %self.salary

class Student(SchoolMember):
   '''Represents a student.'''
  def __init__(self,name,age,marks):
      SchoolMemeber.__init__(self,name,age):
    self.marks=marks
    print '(Initialized Student: %s)' %self.name
  def tell(self):
    SchoolMember.tell(self)
    print 'marks: "%d"' %self.marks
t=Teacher('aaa','28',1234)
s=Student('bbb','29',5678)


