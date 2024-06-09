class Student:
    def __init__(self,name = None , id = None , dep = None ) -> None:
        self.name = name 
        self.id = id 
        self.dep = dep 
        self.email = None 
        self.password  = None 
        print("Student object is created!")

            
class Usis: 
    def __init__(self) -> None:
        self.flag = True
        print("USIS is ready to use!") 
    def login(self,obj)-> str :
        if  obj.email == None  or  obj.password == None  :
            print("Email and password need to be set.")
        elif  obj.email != None  and obj.password != None  :
            print("Login successful!")
    def advising(self , *arg):
        if len(arg)== 1:
            print("You haven't selected any courses.")
        elif len(arg) > 4 :
            print("You need special approval to take more than 3 courses")
        else:
            self.list_f_course = list(arg)[1:]
            print(self.list_f_course)
    def individualDetails(self,obj)-> str :
        return(
            
            f"Name : {obj.name}\nID: {obj.id}\nDepartment: {obj.dep}\nAdvised courses: {','.join(self.list_f_course)}"
        )

rakib = Student("Rakib", 12301455, "CSE")
print("1***********************")
usis_obj = Usis()
print("2***********************")
usis_obj.login(rakib)
print("3***********************")
usis_obj.advising(rakib)
print("4***********************")
rakib.email = "rakib@hotmail.com"
rakib.password = "1234"
print("5***********************")
usis_obj.login(rakib)
print("6***********************")
usis_obj.advising(rakib)
print("7***********************")
usis_obj.advising(rakib, "CSE110", "PHY111", "MAT110", "CSE260")
print("8***********************")
usis_obj.advising(rakib, "CSE110", "PHY111", "MAT110")
print("9***********************")
print(usis_obj.individualDetails(rakib))
