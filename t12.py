def TowerOfHanoi(n , a, b,c):           
    if n == 1:
        print(a,b)
        return
    TowerOfHanoi(n-1, a,c, b)
    print(n,"from",a,"to",b)
    TowerOfHanoi(n-1, c, b, a)
n=int(input())
TowerOfHanoi(n, 'A', 'C', 'B')
