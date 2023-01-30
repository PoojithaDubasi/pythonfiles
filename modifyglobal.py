var1="hi"
def abc():
    global var1
    var1="good morning"
    print("in the function var1 is: ",var1)
abc()
print("outside the function is var1: ",var1)
var1="very good"
print("outside function after modifying is:",var1)