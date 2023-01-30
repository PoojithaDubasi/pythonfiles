'''write a non-repeated character in a string 
example: i/p: 1.level
         o/p: 2. v'''
str='le l'
for i in str:
    count=0
    for j in str:
        if i==j:
            count+=1
        if count>1:
            break
    if count==1:
        print('the non-repeated char is ',i)  