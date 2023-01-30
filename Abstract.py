#Abstract class
#it is the process of handling  the information by hiding
#INFORMAL OF UNNECESSARY INFORMATION OF THE USER
class fruit:
    def taste(self):
        raise NotImplementedError()
    def rich(self):
        raise NotImplementedError()
    def color(self):
        raise NotImplementedError()
class mango(fruit):
    def taste(self):
        return "sweet"
    def rich(self):
        return "vitamin A"
    def color(self):
        return "Yellow"
class orange(fruit):
    def taste(self):
        return "sweet"
    def rich(self):
        return "vitamin c"
    def color(self):
        return "orange"
Alphanso=mango()
print(Alphanso.taste(),Alphanso.rich(),Alphanso.color())
orange=orange()
print(orange.taste(),orange.rich(),orange.color()) 