#program to illustrate the constructor
#__int__().....method
class abc:
    def __init__(self, val):
        print("in class method")
        self.val=val
        print("thr value is :",val)
obj=abc(10)


