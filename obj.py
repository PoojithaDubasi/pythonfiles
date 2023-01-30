#program to access a class var using a class object
'''
class abc:
    var=22
obj = abc()
print(obj.var)'''
#program to access a class memeber using a class object
class abc:
    var=22
    def display(self):
        print("this is class method")
obj = abc()
print(obj.var)
obj.display()
