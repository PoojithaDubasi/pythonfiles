#prime numbers between given two numbers
s=int(input("start number"))
e=int(input("end number"))
for s in range(s,e,1):
    i=1
    c=0
    for i in range(i,s+1,1):
        if (s)%i==0:
            c=c+1
    if c==2:
        print("{}".format(s))