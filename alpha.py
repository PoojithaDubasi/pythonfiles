'''a=65
r=7
for i in range(0,r):
    for j in range(0,i+1):
        ch=chr(a)
        print(ch,end=" ")
        a+=1
    print('')'''   
#for equilateral
a=65
r=7
m=(2*a)-2
for i in range(0,r):
    for j in range (0,m):
        print(end=" ")
    m=m-1
    for j in range (0,i+1):
        ch=chr(a)
        print(ch,end=" ")
        a+=1
    print(" ")