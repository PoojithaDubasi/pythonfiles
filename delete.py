#delete method ---c++/java analoges to destruction
#general syntax___del___
class abc():
    class_var=0
    def __init__(self,var):
        abc.class_var +=1
        self.var=var
        print("the object value is ",var)
        print("the class value is ",abc.class_var)
        
    def __del__(self):
        abc.class_var -=1
        print("the object with value %d  is going out of scope ",self.var)
obj1=abc(10)
obj2=abc(11)
obj3=abc(12)
del obj1
del obj2
del obj3