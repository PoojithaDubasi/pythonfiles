#to visualize ineritance flow
class person:
    def _init_(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name is ",self.name)
        print('age is',self.age)
class teacher(person):
    def __init__(self,name,age,exp,rarea):
        person._init_(self,name,age)
        self.exp=exp
        self.rarea=rarea
    def displaydata(self):
        person.display(self)
        print('experience is',self.exp)
        print('research area',self.rarea)
class student(person):
    def __init__(self,name,age,course,marks):
        person._init_(self,name,age)
        self.course=course
        self.marks=marks
    def displaydata  (self):
        person.display(self)
        print('courses=',self.course)
        print('marks=',self.marks)
print('------teacher class-------')
T=teacher('marks',43,20,'JSS')
T.displaydata()
print('-------student class--------')
S=student('sophie',20,'B.E',78)
S.displaydata()