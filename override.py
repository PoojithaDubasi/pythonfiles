#program to over-ride get-item and set-item methods
class mylist:
    def __init__(self,list):
        self.list=list
    def __getitem__(self,index):
        return self.list[index]
    def __setitem__(self,index,num):
        self.list[index]=num
    def __len__(self):
        return len(self.list)
    def display(self):
        print(self.list)
L=mylist([1,2,3,4,5,6,7,8,9])
print("list is:")
L.display()
index=int(input("enter the index: "))
print("index value is:",L[index])
num=int(input("enter the position u want to modify:"))
L[index]=num
L.display()
print("the length of list is:",len(L))