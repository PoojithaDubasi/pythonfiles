#method by using sum
def Ls(string):
    return sum(1 for i in string)
string='india'
print(Ls(string))
#counter method
def Ls(str):
    c=0
    for i in str: #while str[c:]
        c+=1
    return c
str="SRU"
print(Ls(str))
#using join and count
def Ls(str1):
    if not str1:
        return 0
    else:
        r_str1='py'
        return((r_str1).join(str1).c(r_str1)+1)
str='india'
print(Ls(str1))