class Bird :
    def __init__(self,name , fly = False ) -> None:
        self.name = name 
        self.Fly = fly 
        self.type = None 
    def fly(self):
        if not self.Fly :
            print(f"{self.name } can not Fly ")
        else:
            print(F'{self.name} can Fly')
            
    def setType(self, type ):
        self.type= type 
        
    def printDetail(self):
        print(f"Name: {self.name}\
\nType: {self.type}")
        





ostrich = Bird('Ostrich')
duck = Bird("Duck", True)
owl = Bird('Owl', True)
print('###########################')
ostrich.fly()
duck.fly()
owl.fly()
duck.setType('Water Birds')
owl.setType('Birds of Prey')
print('=========================')
ostrich.printDetail()
print('=========================')
duck.printDetail()
print('=========================')
owl.printDetail()
        