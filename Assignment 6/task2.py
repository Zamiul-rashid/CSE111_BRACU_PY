class Passenger:
    count = 0
    def __init__(self,name) -> None:
        self.name = name
        self.price = 450 
        Passenger.count += 1
    def set_bag_weight(self,weight):
        self.weight = weight
        if self.weight < 20:
            self.price += 0 
        elif self.weight >= 20 and self.weight <= 50:
            self.price += 50 
        elif self.weight > 50:
            self.price += 100
    def printDetail(self):
        print(f"Name: {self.name}\nBag Weight: {self.weight}\nPrice: {self.price}")
            
# Write your code here
    
print("Total Passenger:", Passenger.count)
p1 = Passenger("Jack")
p1.set_bag_weight(90)
p2 = Passenger("Carol")
p2.set_bag_weight(10)
p3 = Passenger("Mike")
p3.set_bag_weight(25)
print("=========================")
p1.printDetail()
print("=========================")
p2.printDetail()
print("=========================")
p3.printDetail()
print("=========================")
print("Total Passenger:", Passenger.count)
            

            
        