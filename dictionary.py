'''write a program to combine list to a dictionary to form a hash table
input: keys=['name','age','branch']
       values=['ABC','100','aeronautical']'''
keys=['name','age','branch']
values=['ABC',100,'aeronautical']
outsource=zip(keys,values)
abc=dict(outsource)
print(abc)