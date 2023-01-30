# program to differntiate between class and obj variable
class abc():
    class_var=0 # it is class variable
    def __init__(self,var):
        abc.class_var += 1
        self.var = var #object variable-which we are passing arguments from class to object
        print("the obj var is:",var)
        print("class value of c=var",abc.class_var)
obj1=abc(10)
obj2 = abc(20)
obj3= abc(30)