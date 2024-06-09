class Spaceship:
    def __init__(self,name,limit):
        self.name = name 
        self.limit = limit 
        self.load=0
        self.item=[]
        
    def load_cargo(self,load2):
        calc = load2.getload() - (self.limit-self.load) 
        self.load += load2.getload() 
        if self.load>self.limit:
            print(f"Warning: Unable to load {load2.getname()} inside {self.name}. Exceeds capacity by {calc}.") 
        else:
            self.item.append(load2.getname())    
    
    def display_details(self):
        print(f"Spaceship Name: {self.name} \nCapacity: {self.limit} \nCurrent Cargo Weight: {self.load} \nCargo: {self.item}")

    
class Cargo:
    
    def __init__(self,name,weight):
        self.__mat = name  
        self.__weight = weight 
        
    def getload(self):
        return self.__weight   
    
    def getname(self):
        return self.__mat  
    


# Creating spaceships
falcon = Spaceship("Falcon", 50000)
apollo = Spaceship("Apollo", 100000)
enterprise = Spaceship("Enterprise", 220000)
print("1.===================================")
# Creating cargo
gold = Cargo("Gold", 20000)
platinum = Cargo("Platinum", 25000)
dilithium = Cargo("Dilithium", 50000)
trilithium = Cargo("Trilithium", 70000)
neutronium = Cargo("Neutronium", 80000)
print("2.===================================")
# Loading cargo onto spaceships
falcon.load_cargo(gold)
falcon.load_cargo(platinum)
falcon.display_details()
print("3.===================================")
apollo.load_cargo(gold)  # Apollo will not reach its total capacity
apollo.display_details()
print("4.===================================")
falcon.load_cargo(neutronium)  # This should exceed Falcon's capacity
print("5.===================================")
enterprise.load_cargo(dilithium)
enterprise.load_cargo(trilithium)
enterprise.load_cargo(neutronium)  # This should not exceed Enterprise's capacity
enterprise.display_details()
enterprise.load_cargo(gold)
enterprise.display_details()