#write a python application to display formate as A
for r in range(7) :
    for c in range(5):
        if r==0 and (c in {1,2,3}):
            print("*", end=" " )
        elif r==3:
            print("*",end=" ")
        elif( r in {1,2,4,5,6}) and (c in {0,3}):
            print("*", end=" " )
        else:
            print("  ",end=" ")
    print()