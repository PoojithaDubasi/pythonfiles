'''You are playing an online game. In the game, a list of N numbers is given. The player has to arrange the numbers
so that all the odd numbers of the list come after the even numbers. Write an algorithm to arrange the given list
such that all the odd numbers of the list come after the even numbers.
Input
The first line of the input consists of an integer numbers, representing the size of the list(N).
The second line of the input consists of N space-separated integers representing the values of the list
Output
Print N space-separated integers such that all the odd numbers of the list come after the even numbers
Example:
Sample Input
8
10 98 3 33 12 22 21 11
Sample Output
10 98 12 22 3 33 21 11'''
n=int(input())
if(n<=0):
    print("Invalid Input")
    quit()
x=input().split()
x=[int(i) for i in x]
o=[]
e=[]
for i in range(0,n):
    if(x[i]%2==0):
        e.append(x[i])
    else:
        o.append(x[i]) 

#e.sort()
#o.sort()
x=[]
l=e+o
for i in l:
    print(i,end=" ")