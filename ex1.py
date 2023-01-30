for r in range(5):
    for c in range(4):
        if (r in {0,2,4}) and (c in {0,1,2}):
            print("*",end=" ")
        elif (r in {1,3}) and (c in {0,3}):
            print("*",end=" ")
        else:
            print(" ",end=" ")
print()