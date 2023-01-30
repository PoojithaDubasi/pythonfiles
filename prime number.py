num=int(input("read n value: "))
f=0
if num > 1:
    for i in range(1,num+1,num):
        if(num % i) == 0:
            f= f+1
            break
if f==2:
    print("{} is a composite number".format(num))
else:
    print("{} is a prime number ".format(num))