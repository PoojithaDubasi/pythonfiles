#mirror right angle
'''n=int(input())
for i in range(n,0,-1):
    for j in range(0,i):
          print(j+1,end=" ")
    print("\n")'''
        
n=int(input())
for i in range(n+1,0,-1):
    for j in range(1,n+1):
          if(j<i):
            print(' ',end=" ")
          else:
            print((j-i)+1,end=" ")#print("*",end=" ")
    print("\n")