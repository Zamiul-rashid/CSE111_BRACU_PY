class Teacher:
    def __init__(self, name, department):
        self.__name = name
        self.__department = department
        self.__courses = []

    def addCourse(self, course):
        self.__courses.append(course)

    def printDetail(self):
        print("=" * 34)
        print("Name: ", self.__name)
        print("Department: ", self.__department)
        print("List of courses")
        print("=" * 34)
        for course in self.__courses:
            print(course.title)
        print("=" * 34)


class Course:
    def __init__(self, title):
        self.title = title

        
        
        
t1 = Teacher("Saad Abdullah", "CSE")
t2 = Teacher("Mumit Khan", "CSE")
t3 = Teacher("Sadia Kazi", "CSE")                          
c1 = Course("CSE 110 Programming Language I")                           
c2 = Course("CSE 111 Programming Language-II")                           
c3 = Course("CSE 220 Data Structures")                           
c4 = Course("CSE 221 Algorithms")                           
c5 = Course("CSE 230 Discrete Mathematics")                           
c6 = Course("CSE 310 Object Oriented Programming")                           
c7 = Course("CSE 320 Data Communications")                          
c8 = Course("CSE 340 Computer Architecture") 
t1.addCourse(c1)
t1.addCourse(c2)
t2.addCourse(c3)
t2.addCourse(c4)
t2.addCourse(c5)
t3.addCourse(c6)
t3.addCourse(c7)
t3.addCourse(c8)
t1.printDetail()
t2.printDetail()
t3.printDetail()
