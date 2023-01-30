class polygon:
    def get_data(self):
        raise notImplementedError()
    def area(self):
        raise notImplementedError()
class rectangle(polygon):
    def get_data(self):
        self.length=float(input("enter rectangle len:"))
        self.breadth=float(input("enter rectangle breadth:"))
    def area(self):
        return self.length*self.breadth
class triangle(polygon):
    def get_data(self):
        self.base=float(input("enter the base of triangle:"))
        self.height=float(input("enter the height of triangle:"))
    def area(self):
        return 0.5*self.base*self.height
r=rectangle()
r.get_data()
print("area of rectangle",r.area())
t=triangle()
t.get_data()
print("area of triangle",t.area())