#program to demonstrate get and set items in a list
class numbers:
    def __init__(self,mylist):
        self.mylist=mylist
    def __getitem__(self,index):
        return self.mylist[index]
    def __setitem__(self,index,val):
        self.mylist[index]=val
numlist = numbers([1,2,3,4,5,6,7,8])
print(numlist[3])
numlist[3]=10
print(numlist.mylist)
print(numlist[3])