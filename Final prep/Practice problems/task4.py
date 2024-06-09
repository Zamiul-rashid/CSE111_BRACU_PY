class Account:
    count = 0 
    def __init__(self, name , age , job,selary) -> None:
        Account.count+=1 
        self.name= name 
        self.age = age 
        self.job = job 
        self.balance  = selary 
        
    def addMoney(self, amount ):
        self.balance+= amount 
        
    def withdrawMoney(self,amount):
        if amount > self.balance:
            # print()
            pass 
        else :
            # print()
            self.balance-= amount 
            
    def printDetails(self):
        print(F'''Name: {self.name}
Age: {self.age}
Occupation:  {self.job}
Total Amount:  {self.balance}''')




print('No of account holders:', Account.count)
print("=========================")
p1 = Account("Abdul", 45, "Service Holder", 500000)
p1.addMoney(300000)
p1.printDetails()
print("=========================")
p2 = Account("Rahim", 55, "Businessman", 700000)
p2.withdrawMoney(700000)
p2.printDetails()
print("=========================")
p3 = Account("Ashraf", 62, "Govt. Officer", 200000)
p3.withdrawMoney(250000)
p3.printDetails()
print("=========================") 
print('No of account holders:', Account.count)
