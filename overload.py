#program to overloaded the_call_method
class multi:
    def __init__(self,num):
        self.num=num
    def __call__(self,o):
        return self.num*o
x=multi(10)
print(x(5))