def eo(n):
    if a%2==0:
        return 1
    else:
        return -1
a=int(input())
flag=eo(a)
if flag==1:
    print("even")
else:
    print("odd")