class Tournament:
    
    def __init__(self,name='Default',no = 0, Type = 'No type'):
        self.__name = name
        self.__type = Type
        self.Number_of_teams = no
        
    def set_name(self,name):
        self.__name = name
        
    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type
    
        
class Cricket_Tournament(Tournament):
    def __init__(self,name='Default',no = 0, Type = 'No type'):
        super().__init__(name , no , Type)
        
    def detail(self):
        return(f"Cricket Tournament Name: {self.get_name()} \
            \nNumber of teams: {self.Number_of_teams} \
            \nType: {self.get_type()}")
    
class Tennis_Tournament(Tournament):
    def __init__(self, name='Default', no=0, Type='No type'):
        super().__init__(name, no, Type)
    
    def detail(self):
        return(f"Tennis Tournament Name: {self.get_name()} \
            \nNumber of teams: {self.Number_of_teams}")          
    

ct1 = Cricket_Tournament()
print(ct1.detail())
print("-----------------------")
ct2 = Cricket_Tournament("IPL",10,"t20")
print(ct2.detail())
print("-----------------------")
tt = Tennis_Tournament("Roland Garros",128)
print(tt.detail())

    
    
