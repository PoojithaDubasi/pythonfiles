n=int(input())
list=[]
for i in range(0,n+1):
    a=2**i
    list.append(a)
    b=3**i
    list.append(b)
print(list)
num=int(input("enter the position: "))
print(list[num-1])
l=len(list)
print(list[l-1])