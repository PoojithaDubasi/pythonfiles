'''write a python program to print a specified list after removing the 0Th,4th and 5th elements.
sample list:      ['red','green','white','black','pink','yellow']
expected output:  ['green','white','black']'''
l=input().split()
s=[]
for i in range(len(l)):
    if i==0 or i==4 or i==5:
        continue
    else:
        s.append(l[i])
print(s)