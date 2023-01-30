#program to illustrating a modification on numerics
class Number:
    even=0
    def check(self,num):
        if num%2==0:
            self.even=1
    def even_odd(self,var):
        self.check(num)
        if self.even==1:
            print(num,"is even")
        else:
            print(num,"is odd")
#num=int(input())
obj=Number()
obj.even_odd(num)