#program to find thes um of digits in a number
#123=1+2+3=6
num=int(input())
n=num
sum=0
while(num!=0):
    rem=num%10
    sum=sum+rem
    num=num//10
print(sum)
d=n//sum
print(d)