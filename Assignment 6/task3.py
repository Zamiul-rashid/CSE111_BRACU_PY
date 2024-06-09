class Travel :
    count = 0
    def __init__(self,city1,city) -> None:
        self.city1 = city1  
        self.city = city
        self.F_time = "1:00"
        Travel.count += 1
        
    def set_time(self,time):
        self.F_time = f"{str(time)}:00"
        
    def set_destination(self,city):
        self.city = city
        
    def set_source(self,city):
        self.city1 = city
        
    def display_travel_info(self):
        return(f"Source: {self.city1}  \nDestination: {self.city} \nFlight Time: {self.F_time}")
    
    
 
print("No. of Traveller =", Travel.count)
print("=======================")
t1 = Travel("Dhaka","India")
print(t1.display_travel_info())
print("=======================")
t2 = Travel("Kuala Lampur","Dhaka")
t2.set_time(23)
print(t2.display_travel_info())
print("=======================")
t3 = Travel("Dhaka","New_Zealand")
t3.set_time(15)
t3.set_destination("Germany")
print(t3.display_travel_info())
print("=======================")
t4 = Travel("Dhaka","India")
t4.set_time(9)
t4.set_source("Malaysia")
t4.set_destination("Canada")
print(t4.display_travel_info())
print("=======================")
print("No. of Traveller =", Travel.count)     