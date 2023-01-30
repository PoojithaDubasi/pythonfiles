#write a program to caliculation SI .supposemthe customer is a senior citizen, he is being offered
#12% ROI for all other customers,the roi is 10%
def SI():
    if age>=60:
        ROI=0.12
    else:
        ROI=0.01
    si=p*r*ROI/100
    print("simple interest: ",si)
p=200
r=3
age=int(input())
SI()