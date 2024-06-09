class Monster:
    monstercount  = 0 
    def __init__(self,NAME , power) -> None:
        Monster.monstercount+=1 
        self.name = NAME 
        self.power = power 
        self.alive = True 
        
    def get_details(self):
        return(F"""Name:{self.name}
Power:{self.power}
Alive:{self.alive}""")

    def attack(self,other):
        if self.alive :
            if self.power > other.power:
                other.alive = False 
            else:
                self.alive = False 
                
        else:
            print(f"{other.name} is not alive to attack.")
            return
        
monster1 = Monster('Godzilla', 40)
monster2 = Monster('Hydra', 30)
monster3 = Monster('KingKong', 50)
print(f"Number of monsters
alive:{Monster.monsterCount}")
print('1--------------------------------')
print(monster1.get_details())
print('2--------------------------------')
print(monster2.get_details())
print('3--------------------------------')
print(monster3.get_details())
print('4--------------------------------')
monster1.attack()
print('5--------------------------------')
monster1.attack(monster2)
print('6--------------------------------')
monster1.attack(monster2, monster3)
print('7--------------------------------')
print(f"Number of monsters
alive:{Monster.monsterCount}")
print('8--------------------------------')
print(monster2.get_details())
print('9--------------------------------')
monster2.attack(monster1)