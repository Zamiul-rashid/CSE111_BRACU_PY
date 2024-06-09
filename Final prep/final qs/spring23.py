class ChefsCounter:
    reservation = {}

    def __init__(self, name, reservation_limit=5):
        self.name = name
        self.reservation_limit = reservation_limit
        self.customer_list = []
        print(f"The {self.name} branch of Chef's Counter is open for reservation!")
        
    def reserve(self, *args):
        for customer in args:
            if len(self.customer_list) < self.reservation_limit:
                self.customer_list.append(customer)
            else:
                print(f"Sorry {self.name}, {self.reservation_limit} people already made a reservation in this branch.")
        if len(self.customer_list)< self.reservation_limit:
            return
        if self.name in ChefsCounter.reservation:
            ChefsCounter.reservation[self.name].extend(self.customer_list)
        else:
            ChefsCounter.reservation[self.name] = self.customer_list

    def reservation_info(self):
        if self.name in ChefsCounter.reservation:
            print(f"Customers who reserved in {self.name} branch: {', '.join(ChefsCounter.reservation[self.name])}")
        else:
            print(f"No reservations found for {self.name} branch.")

    @classmethod
    def create_new_branch(cls, other):
        return ChefsCounter(other)

print("===============1=============")
branch1 = ChefsCounter("Gulshan")
print("===============2=============")
branch1.reserve("Sam", "Paul")
print("===============3=============")
branch1.reservation_info()
print("===============4=============")
branch1.reserve("John", "Robin", "Billy", "Robert")
print("===============5=============")
branch1.reservation_info()
print("===============6=============")
branch2 = ChefsCounter("Dhanmondi", 7)
print("===============7=============")
branch2.reserve("Ben", "Alice", "Fred")
print("===============8=============")
branch2.reservation_info()
print("===============9=============")
branch2.reserve("Tom", "Ken", "Garet", "Miles", "Taylor")
print("===============10=============")
branch2.reservation_info()
print("===============11=============")
branch3 = ChefsCounter.create_new_branch("100feet")
print("===============12=============")
branch3.reserve("Harry", "Bob", "Jenny")
print("===============13=============")
branch3.reservation_info()
print("===============14=============")
print("Reservation Information of All Branches:", ChefsCounter.reservation)