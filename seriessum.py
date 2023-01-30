'''#series sum 1+1/2+1/3+1/4+.....1/n
n=int(input("enter the nth term"))
s=0.0
for i in range(1,n+1):
    a=1.0/i
    s=s+a
print("the sum of series  1,1/2,.....1/"+ str(n)+" is",s)'''
n=int(input("enter the nth term"))
s=0.0
for i in range(1,n+1):
    a=1.0/(i**2)
    s=s+a
print("the sum of series  1,1/2,.....1/"+ str(n)+" is",s)