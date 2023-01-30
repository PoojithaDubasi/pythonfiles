#is for ilustrating use of a private methods
'''
class abc:
    def __init__(self,var):
        self.__var=var
    def __display(self):
        print("this is from clas method var=",self.__var)
obj =abc(10)
obj._abc__display()'''
#to call a class method from another method of same class
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is :",self.var)
    def add_2(self):
        self.var+=2
        self.display()
obj = abc(10)
obj.add_2()
        