#program to show how a class method calls a function which defined in th global name space
def scale_10(x):
    return x*10
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is: ",self.var)
    def modify(self):
        self.var =scale_10(self.var)
obj =abc(10)
obj.display()
obj.modify()
obj.display()