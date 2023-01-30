#write a program to remove an empty tuple from list of tuples
def remove(tuples):
    tuples=[t for t in tuples if t]
    return tuples
tuples=[(),('poojitha',14),(),('teju',15)]
print(remove(tuples))