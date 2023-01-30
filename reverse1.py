s=input("read any string:")
l=len(s)
i=l-1
rev=''
while i>=0 :
    rev=rev+s[i]
    i=i-1
    print("reverse of give {} is {}".format(s,rev))