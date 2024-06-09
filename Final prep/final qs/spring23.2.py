class Ticket:
    route_distance = {"Route A": 400, "Route B": 425, "Route C": 350}
    fare_per_km = 20

    def __init__(self, route, journeyDate, price=0):
        self.route = route
        self.journeyDate = journeyDate
        self.__price = price

    def setPrice(self, price):
        self.__price = price

    def getPrice(self):
        return self.__price

    def ticket_details(self):
        return f"Route: {self.route}\nJourney Date: {self.journeyDate}"
class BusTicket(Ticket):
    total_tickets = 0
    def __init__(self , route , date , name , seat_num):
        super().__init__(route , date ,(Ticket.route_distance[route]*Ticket.fare_per_km))
        self.name = name 
        self.seat = seat_num
        self.paid = False 
        self.__class__.total_tickets+=1
        # print(f"Total ticket(s): {self.__class__.total_tickets}")
        
    def calculate_fare(self):
        print(f"Ticket fare is calculated successfully.")
        self.getPrice()
    
    def make_payment(self):
        self.paid = True 
        
    def ticket_details(self):
        print(f"Ticket ID: {self.name + str(self.__class__.total_tickets)}")
        print(super().ticket_details())
        print(f'Bus Name: {self.name}\
        \nSeat No: {self.seat}\
        \nPrice(tk): {self.getPrice()}\
        \nStatus: {"Paid" if self.paid == True else "Not Paid"} ')   
        

#Driver Code
ticket1 = BusTicket("Route A", "30 April, 2023", "Nabil Enterprise", "F2")
print("Total ticket(s):", BusTicket.total_tickets)
print("1============================")
ticket1.calculate_fare()
print("2============================")
ticket1.ticket_details()
print("3============================")
ticket1.make_payment()
print("4============================")
ticket1.ticket_details()
print("5============================")
ticket2 = BusTicket("Route C", "26 April, 2023", "Hanif Enterprise", "A2")
print("Total ticket(s):", BusTicket.total_tickets)
print("6============================")
ticket2.calculate_fare()
print("7============================")
ticket2.make_payment()
print("8============================")
ticket2.ticket_details()