#program to find smaller number by lambda
def small(a,b):
    if(a<b):
        return a
    else:
        return b
add = lambda x,y:x+y
diff = lambda x,y:x-y
print("smaller of two no: ",small(add(-2,-2),diff(-1,2)))
#program to find increment using lambda
def increment(y):
    return (lambda x:x+1)(y)
a=100
print("a=",a)
print("a after increment")
b=increment(a)
print(b)
#program to pass a lambda as an function
def fun(f,n):
    print(f(n))
twice = lambda x:x*2
triple = lambda x:x*3
fun(twice,4)
fun(triple,3)
##
x=lambda : sum(range(1,11))
print(x())
