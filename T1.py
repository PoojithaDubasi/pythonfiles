''' there is a jar full of candies for sale at a mall counter. Jar has the capacity N, that is jar can contain maximum N candies
when jar is full. At any point of time. Jar can have M no of candies where M<=N candies are served to customers. Jar is never
remain empty as when last k candies are left. Jar if refilled with new candies in such a way that jar get full

write a code to implement above scenerio. Display JAR at counter with available no of candies.Input should be the no of candies
one customer can order at point of time.Update the JAR after each purchase and display JAR at counter.

output should give number of candies sold and updated no of candies in JAR

if input is more than candies in JAR, return:"INVALID INPUT" given,
N=10,where N is num of candies available
k=<15, where k is the no of minimum candies that must be inside jar ever.

example1:(N=10,k=<5)
input value
 3
output value
 no of candies sold:3
 no of candies available:7 '''


N=10
k=int(input())
if (k==0):
    print("INVALID INPUT")
    print("no of candies avaliable:",N)
elif k<=5:
    c=N-k
    print("no of candies sold:",k)
    print("no of candies avaliable:",c)
else:
    print("INVALID INPUT")
    
''' OUTPUT:
3
no of candies sold: 3
no of candies avaliable: 7'''
