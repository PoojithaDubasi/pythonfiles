"""A digital machine generates binary data which consists of a string of 0s and 1s.A maximum signal M, in the data,
consists of the maximum number of either 1s or 0s appearing consecutively inthe  data but M cant be at the
beginning or end of the string."""
n=int(input())
s=(input())
max=0
count=0
flag=0
for i in range(0,n):
    if s[i]=="1":
        count=count+1
        flag=1
    elif(s[i]=="0" and flag==1):
        count=0
        flag=0
    if count>max:
        max=count
print(max)
