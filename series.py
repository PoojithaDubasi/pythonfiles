#program to print the series 1+1/4+1/9+........1/n^2
n=int(input("enter the number of terms: "))
sum=0
for i in range(1,n+1):
    sum=sum+(1/i**2);
print("the sum of series is {}".format(sum))