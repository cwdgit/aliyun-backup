#!/usr/bin/python
zoo=('wolf','elephant','penguin')
print 'Number of animals in the zoo is',len(zoo)
new_zoo = ('monkey','dolphin',zoo)
print 'Number of animals in the new zoo is',len(new_zoo)
print 'All animals in new zoo are',new_zoo
print 'Animals brought from old zoo are',new_zoo[2]
print 'Animals brough from new zoo are',new_zoo[0],new_zoo[1]
print 'Last animal brought frmo old zoo is',new_zoo[2][2]


