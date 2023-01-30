#to calculate the product,multiplying all the numbers of a given tuple
t=input().split()
t=(int(i) for i in t)
prod=1
for i in t:
    prod=prod*i
print(prod)