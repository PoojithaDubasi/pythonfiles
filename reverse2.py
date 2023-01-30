s=input("read a n string: ")
l=s.split()
l1=[]
for i in l:
    l1.append(i[::-1])
output=''.join(l1)
print("reverse is {}".format(output))