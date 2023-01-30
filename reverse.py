'''n=input("read any n value:")
t=n
rev=n[::-1]
print("reverse of {} is {}".format(t,rev))'''
#recursive
def reverse(n):
    if(len(n))==0:
        return n
    return reverse(n[1:])+n[0]
num=1234
n_string=str(num)
r_num=reverse(n_string)
print("reversednumber:"+r_num)