class PlayerEarning :
    def __init__(self,name):
        self.name = name 
        
    def calculateTotal(self,earnning , goals = None):
        self.earn = earnning
        self.withbonus = earnning
        if goals != None :
            if goals>30 :
                a = (5/100) * earnning + 10000
            else:
                a = (5/100) * earnning
            self.withbonus += a 
            
       
    
    def printDetails(self):
        print(f"""Player Name: {(self.name)}
Player Season Earning without bonus: {int(self.earn)}
Bonus: {int(self.withbonus)-int(self.earn)}
Player Season Earning After Bonus: {int(self.withbonus)}
""") 

print("**********************")
player1 = PlayerEarning('Buffon')
player1.calculateTotal(250000)
player1.printDetails()

print("\n**********************")
player2 = PlayerEarning('Dybala')
player2.calculateTotal(250000, 31)
player2.printDetails()

print("\n**********************")
player3 = PlayerEarning('Cuadrado')
player3.calculateTotal(250000, 20)
player3.printDetails()
