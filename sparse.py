'''write a program to store a sparse matrix in a dictionary
example:[[0,0,0,1,0],
         [2,0,0,0,1],
         [0,0,0,4,0]]'''
matrix=[[0,0,0,1,0],
        [2,0,0,0,3],
        [0,0,0,4,0]]
'''Dict={}
print("Sparse Matrix")
for i in range (len(matrix)):
     print("\n")
     for j in range(len(matrix[i])):
         print(matrix[i][j],end=' ')
         if matrix[i][j]!=0:
            Dict[(i,j)]=matrix[i][j]
print("\n\n Sparse Matrix can be efficiently represented as Dictionary :")
print(Dict)'''
a=[[0,0,0,1,0],[2,0,0,0,3],[0,0,0,4,0]]
d={}
for i in range(len(a)):
    for j in range(len(a[i])):
        if(a[i][j]!=0):
            d[i,j]=a[i][j]              
print(d)