'''write a program to return the full name of a person where 1st  variable passed is first name
2nd variable passed is last name'''
def name(fn,sn):
    s=' '
    n=fn+s+sn
    print("full name: ",n)
fn=str(input())
sn=str(input())
name(fn,sn)