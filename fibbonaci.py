#program to find the exp(x,y)using recurrsion function
def  fibbo(n):
    if n<2:
        return 1
    return (fibbo(n-1)+fibbo(n-2))
n=int(input())
for i in range(n):
    print("fibbonaci(",i,")=",fibbo(i))