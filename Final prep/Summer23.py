class Course:
    total_courses = 0
    def __init__(self,name , name2 ) -> None:
        self.code = name 
        self.name = name2
        Course.total_courses += 1




class Student:
    L_of_course = []
    def __init__(self , name , id , gpa):
        self.name = name 
        self.id = id 
        self.gpa = gpa 
        self.__limit = None 
        self.course_taken = []
    def addCourses(self , *args):
        if self.__limit != None :
            for i in args :
                if len(self.course_taken) < self.__limit :
                    print(f"{i.code} added to course list.")
                    self.course_taken.append(i.code)
                else :
                    print(f"Cannot add {i.code}. Limit exceeded.")
                    
        else:
            print("Sorry. Total course limit is not set.")
            
    def setLimit(self):
        if self.gpa >= 3.5 :
            self.__limit = 5
        elif self.gpa <=2:
            self.__limit = 2
        else:
            self.__limit = 4
    
    def printDetails(self):
        print(f"Student ID: {self.id}\
            \nStudent Name: {self.name}\
                    \nCourses: {self.course_taken}")
        
    def getLimit(self):
        return self.__limit
        
        
print(f"Number of courses:{Course.total_courses}")
print("1--------------------------")
c1 = Course("CSE220", "Data Structures")
c2 = Course("CSE230", "Discrete Mathematics")
c3 = Course("CSE250", "Circuits and Electronics")
c4 = Course("MAT120", "Mathematics II")
c5 = Course("PHY112", "Principles of Physics II")
c6 = Course("STA201", "Statistics I")
c7 = Course("ENG102", "English Composition")
print("2--------------------------")
print(f"Number of courses:{Course.total_courses}")
print("3--------------------------")
s1 = Student("Alice",3242544,2.39)
s2 = Student("Bob",9878686,3.92)
s3 = Student("Carol",2346678,1.67)
print("4--------------------------")
s1.addCourses(c1,c2)
print("5--------------------------")
s1.setLimit()
print("6--------------------------")
print(f"Course limit of {s1.name}is:{s1.getLimit()}")
s1.addCourses(c4,c5,c7)
print("7--------------------------")
s1.addCourses(c1,c2)
print("8--------------------------")
s1.printDetails()
print("9--------------------------")
s2.setLimit()
s3.setLimit()
print("10--------------------------")
print(f"Course limit of {s2.name}is:{s2.getLimit()}")
print(f"Course limit of {s3.name}is:{s3.getLimit()}")
print("11--------------------------")
s2.addCourses(c1,c2,c4,c5,c7)
print("12--------------------------")
s3.addCourses(c2,c4,c5,c7)
print("13--------------------------")
s1.printDetails()
print("14--------------------------")
s2.printDetails()
print("15--------------------------")
s3.printDetails()