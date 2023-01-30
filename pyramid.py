#write a python application to display the stars (*) in pyranid shape
n=int(input("read the no of rows: "))
for i in range(0,n):
    for j in range(0,n-i):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()