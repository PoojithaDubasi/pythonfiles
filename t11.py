n=int(input("N="))
for i in range(1,(n+1)):
    for j in range(1,n+1):
        if(j==n-i+1):
            print("*",end=" ")
        elif(i==j):
            print("*",end=" ")
        elif(i==1 or i==n or j==1 or j==n):
            print("*",end=" ")
        elif(i<j and j<n-i+1):
            print("*",end=" ")
        elif(i>j and j>n-i+1):
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()