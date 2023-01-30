#right angle pattern
'''
n=int(input(" read number of rows: "))
i=1
t=0
while i<=n:
    j=1
    while j<=i:
        print("*",end=' ')
        t=t+1
        j=j+1
    i=i+1
    print()
'''
#right angle pattern    
n=int(input())
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ") #print("*",end=" ")
    print("\n")
