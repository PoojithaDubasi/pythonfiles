#write a program to add elements between a range of m&n
m=int(input())
n=int(input())
sum=0
while(m<=n):
    sum=sum+m
    m+=1
print("sum:",sum)