class Student:
    def __init__(self,name , id , gpa ) -> None:
        self.name = name    
        self.__id = id 
        self.__cgpa = gpa 
        
    def get_id(self) -> int:    
        return self.__id
    # def get_name(self) -> str:
        # return self.name    (na dileo hobe)
    def get_cgpa(self) -> int:
        return self.__cgpa
    
    def setId(self , id):           
        self.__id = id 
        
        

class Department():
    def __init__(self,name) -> None:
        self.students = []
        self.id_list = []   
        self.dep = name 
        
    def addStudent(self, *arg):
        for i in arg:
            if i.get_id() in  self.id_list:
                print("Student with the same ID already exists, Please try with another ID")
                return
            else:
                self.id_list.append(i.get_id())
        # self.id_list.extend([[i.get_id() for i in arg]])
        self.students.extend(arg)
        for i in arg:
             print(f"Welcome to CSE department, {i.name}")
    
    def findStudent(self , id) -> str:
        if id in self.id_list:
            for i in self.students:
                if id == i.get_id():
                    print(f"Student info:\nStudent Name:{i.name}\nID: {i.get_id()}\CGPA : {i.get_cgpa()}") ;break 
        else:
            print("Student with this ID doesn't exist, Please give a valid ID") 
     
    def details(self)->str:
        print(f"Department Name:{self.dep}")
        print(f'Number of student: {len(self.students)}')
        for i in self.students:
            print(
                f"Student name: {i.name}, ID: {i.get_id()}, cgpa: {i.get_cgpa()}"
            )  
          
        

s1 = Student("Akib", 22301010, 3.29)
s2 = Student("Reza", 22101010, 3.45)
s3 = Student("Ruhan", 23101934, 4.00)
print("1==================================")
cse = Department("CSE")
cse.findStudent(22112233)
print("2==================================")
cse.addStudent(s1,s2,s3)
print("3==================================")
cse.details()
print("4==================================")
cse.findStudent(22301010)
print("5==================================")
s4 = Student("Nakib",22301010,3.22)
cse.addStudent(s4)
print("6==================================")
s4.setId(21201220)
cse.addStudent(s4)
print("7==================================")
cse.details()
print("8==================================")
s5 = Student("Sakib",22201010,2.29)
cse.addStudent(s5)
print("9==================================")
cse.details()



