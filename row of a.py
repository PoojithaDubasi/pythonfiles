n=int(input(" read number of rows: "))
i=1
t=0
while i<=n:
    j=1
    while j<=i:
        print(chr(65+t),end='')
        t=t+1
        j=j+1
    i=i+1
    print()