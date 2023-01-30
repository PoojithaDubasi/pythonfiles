#writing a funtion an return its cubation format
def cube(x):
    return(x*x*x)
num = 15
result = cube(num) #cube(10)
print("cube of",num,"=",result)
#writing a function to understand a mismatch parameter
def abc(x):
    print("hi students",x)
abc(5)#it doesnt pass when fun(5,5)
#writing a function to understand a mismatch parameters
def fun(i):
    print("orange",i)
#j=0
#fun(j)
fun(5+2*10)#for expression
#program to demo key args
def display(str,int_x,float_y):
    print("the string is :",str)
    print("the integer is :",int_x)
    print("the float is :",float_y)
display(float_y=9908.9087,str="poojitha",int_x=15)
#employee
def employ(name,age,salary):
    print("name:",name)
    print("age: ",age)
    print("salary: ",salary)
a="poojitha"
b=15
c=12345
employ(salary=c,name=a,age=b)
