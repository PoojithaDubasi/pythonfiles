#Rock paper sicssor
import random
n=input("Enter your choice:")
l=["Rock","Paper","Scissors"]
s=random.choice(l)
print("Computer choice",s)
if n=="Rock" or n=="rock":
    if s=="Scissors" or s=="scissors":
        print("Player won")
    elif s=="Rock" or s=="rock":
        print("DRAW")
    else:
        print("Computer won")
elif n=="Scissors" or n=="scissors":
    if s=="Paper" or s=="paper":
        print("Player won")
    elif s=="Scissors" or s=="scissors":
        print("DRAW")
    else:
        print("Computer won")
elif n=="Paper" or n=="paper":
    if s=="Rock" or s=="rock":
        print("Player won")
    elif s=="Paper" or s=="paper":
        print("DRAW")
    else:
        print("Computer won")
else:
    print("INVALID INPUT")
