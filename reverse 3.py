s=input("read a n string: ")
l=s.split()
s=len(l)
l1=[]
i=s-1
while i>=0:
    l1.append(l[i])
    i=i-1
output=''.join(l1)
print("reverse is {}".format(output))