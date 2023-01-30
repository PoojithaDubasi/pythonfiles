var1="hi"
def abc():
    global var2
    var2="good morning"
    print("in the function var1 is: ",var1)
abc()
print("outside the function is var2: ",var2)
print("var1 is:",var1)