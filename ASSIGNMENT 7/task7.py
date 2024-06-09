class Fruit:
    Total_order=0
    
    def __init__(self, Order_ID, weight):
        self.Order_ID=Order_ID
        self.weight=weight
        Fruit.Total_order=Fruit.Total_order+1
    
    def __str__(self):
        return self.Order_ID+", Weight: "+str(self.weight)
    
class Mango(Fruit):
    def __init__(self, Order_ID, weight,name, price ):
        super().__init__(Order_ID, weight)
        self.price = price * weight
        self.name = name 
    
    def __str__(self):
        return f"self.Order_ID , Weight: {self.weight}, Variety: {self.name}\nTotal Price: {self.price}"
    
    def __add__(self,other):
        return (f"The total Price of the orders are: {self.price + other.price}")
    
class JackFruit(Fruit):
    def __init__(self, Order_ID, weight ,price ):
        super().__init__(Order_ID, weight)
        self.price = price * weight
    
    def __str__(self):
        return f"self.Order_ID , Weight: {self.weight},Total Price: {self.price}"
    
    def __add__(self,other):
        return (f"The total Price of the orders are: {self.price + other.price}")
        


m1=Mango("Order Id 1", 5,"GopalVog",250)
print(m1)
m2=Mango("Order Id 2", 5,"HariVanga", 230)
print(m2) 
j1=JackFruit("Order Id 3", 5,250)
print(j1)
j2=JackFruit("Order Id 4", 4,210)
print(j2)
print("Total number of Orders: "+str(Fruit.Total_order))
print("==================")
print(m1+m2)
print("==================")
print(j1+j2)
