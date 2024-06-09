class Shape:

  def __init__(self, name='Default', height=0, base=0):
    self.area = 0
    self.name = name
    self.height = height
    self.base = base

  def get_height_base(self):
    return "Height: "+str(self.height)+",Base: "+str(self.base)
#   def printDetails(self):
      

class triangle(Shape):
    def __init__(self, name='Default', height=0, base=0):
        super().__init__(name, height, base)
       
    def calcArea(self):
        self.area = (self.height*self.base)/2
        return self.area
    def printDetail(self):
        return(f"Shape Name: {self.name} \
            \nHeight: {self.height}, Base: {self.base} \
            \nArea: {self.calcArea()}")
class trapezoid(Shape):
    def __init__(self, name='Default', height=0, base=0, upper_base=0):
        super().__init__(name, height, base)
        self.upper_base = upper_base
        
    def calcArea(self):
        self.area = ((self.base + self.upper_base) * self.height) / 2
        return self.area
    
    def printDetail(self):
        return (f"Shape Name: {self.name} "
                f"\nHeight: {self.height}, Base: {self.base}, Side_A: {self.upper_base} "
                f"\nArea: {self.calcArea()}")
        
# write your code here

tri_default = triangle()
tri_default.calcArea()
print(tri_default.printDetail())
print('--------------------------')
tri = triangle('Triangle', 10, 5)
tri.calcArea()
print(tri.printDetail())
print('---------------------------')
trap = trapezoid('Trapezoid', 10, 6, 4)
trap.calcArea()
print(trap.printDetail())
