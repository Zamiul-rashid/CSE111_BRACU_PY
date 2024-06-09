class Train :
    def __init__(self,*arg) -> None:
        self.train = arg[0]
        self.stations = list(arg)[1:]
        self.Passenger_list = []
        print(f"Welcome aboard on {self.train}\
                \nStart: {self.stations[0]}\
                \nDestination: {self.stations[-1]}\
                ")
        
    def allPassengerDetails(self) -> None :
            print("Passenger Details:")
            for passenger in self.Passenger_list:
                if passenger.start == None :
                    passenger.start = self.stations[0]
                    passenger.end = self.stations[-1]
                    # start , end = passenger.start , passenger.end 
                    passenger.fair = (self.stations.index(passenger.start) - self.stations.index(passenger.end))*100
                elif passenger.end == None  :
                    passenger.end = self.stations[-1]
                    passenger.fair = (self.stations.index(passenger.start) - self.stations.index(passenger.end))*100  
                    # start , end = passenger.start , passenger.end          
                elif passenger.start != None and passenger.end != None :
                    passenger.fair = (self.stations.index(passenger.start) - self.stations.index(passenger.end))*100
                    # start , end = passenger.start , passenger.end 
       
                # print(f"Name: {passenger.name}\nStart: {self.calculate(passenger)[1]}\
                #     \nDestination: {self.calculate(passenger)[2]}\
                #     \nFair: ${self.calculate(passenger)[0]}")
     
                print(f"Name: {passenger.name}\nStart: {passenger.start}\
                    \nDestination: {passenger.end}\
                    \nFair: ${passenger.fair}")
     
    def addPassenger(self , *arg ) -> None :
        for i in arg:
            print(f"{i.name} Welcome abroad")
            self.Passenger_list.append(i)
    
        
    # def calculate(self , obj):
    #     if obj.start == None :
    #         obj.start = self.stations[0]
    #         obj.end = self.stations[-1]
    #         start , end = obj.start , obj.end 
    #         fair = (self.stations.index(obj.start) - self.stations.index(obj.end))*100
    #     elif obj.end == None  :
    #         obj.end = self.stations[-1]
    #         fair = (self.stations.index(obj.start) - self.stations.index(obj.end))*100  
    #         start , end = obj.start , obj.end          
    #     elif obj.start != None and obj.end != None :
    #         fair = (self.stations.index(obj.start) - self.stations.index(obj.end))*100
    #         start , end = obj.start , obj.end 
    #     return (fair ,start , end)
                            
class Passenger :
    def __init__(self,*arg) -> None:
        self.name = arg[0];self.fair = 0
        self.start = None 
        if len(arg)== 2 :
            self.start = arg[1]
            self.end = None 
        
        if len(arg) == 3:
            self.start = arg[1]
            self.end = arg[2]
 
            
    
t1 = Train('T1-Express','New York','Manhattan','Brooklyn','Boston')
print("1========================")
p1 =Passenger("Naruto")
t1.addPassenger(p1)
p2 = Passenger("Sasuke","Manhattan")
p3 = Passenger("Hinata","Manhattan","Brooklyn")
print("2========================")
t1.addPassenger(p2,p3)
print("3========================")
t1.allPassengerDetails()
print("4========================")
t2 = Train('Europe-Express','London','Paris','Brussels','Turkey')
print("5========================")
p4 =Passenger("Max","London","Brussels")
p5 = Passenger("Eleven","Paris")
p6 = Passenger("Mike","Brussels")
t2.addPassenger(p4,p5,p6)
print("6========================")
t2.allPassengerDetails()

