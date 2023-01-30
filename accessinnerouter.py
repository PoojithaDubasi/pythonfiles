#program to dem access of var in and outer function
def outer_fun():
    outer_var=11
    def inner_fun():
        inner_var=22
        print("outer varianle",inner_var)
    inner_fun()
    print("inner varianle",outer_var)
outer_fun()