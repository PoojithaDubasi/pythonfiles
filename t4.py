'''n=int(input())
a=b=0
for i in range(1,n+1):
    if(i%2!=0):
        a=a+7
    else:
        b=b+6
if n%2!=0:
    print("{} at accordance{}".format(n,a-7))
else:
    print("{} at accordance{}".format(n,b-6))'''
n=int(input())
list=[]
for i in range(0,n+1):
    a=7*i
    list.append(a)
    b=6*i
    list.append(b)
print(list)
num=int(input("enter the position: "))
print(list[num-1])