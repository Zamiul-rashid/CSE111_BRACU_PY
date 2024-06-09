class Student:
    count = 0 
    count_dep = []
    cse = 0
    bba = 0
    def __init__(self,name , dep ) -> None:
        self.bba = []
        self.cse = []
        self.name = name 
        self.dep = dep 
        Student.count+=1 
        print(F"Creating Student Number: {Student.count}")
        Student.count_dep.append(name)
        if self.dep == "BBA":
            self.bba.append(name)
            Student.bba+=1
        else:
            self.cse.append(name)
            Student.cse+=1

    def individualInfo(self):
        if self.dep == "CSE":     
            print(F'''{self.name} is from {self.dep} department.
Serial of {self.name} among all students' is: {((Student.count_dep.index(self.name))+1)}
Serial of {self.name} in CSE department is: {self.cse.index(self.name)+1}''')
        else:          
            print(F'''{self.name} is from {self.dep} department.
Serial of {self.name} among all students' is: {(Student.count_dep.index(self.name))+1}
Serial of {self.name} in CSE department is: {self.bba.index(self.name)+1}''')
    @classmethod       
    def totalInfo(cls):
        print(F'''Total Number of Student: {cls.count}
Total Number of CSE Student: {cls.cse}
Total Number of BBA Student: {cls.bba}''')

    
        
s1 = Student("Naruto", "CSE")
print('----------------------')
s1.individualInfo()
print('#############################')
s1.totalInfo()
print('============================')


s2 = Student("Sakura", "BBA")
print('----------------------')
s2.individualInfo()
print('#############################')
s2.totalInfo()
print('============================')


s3 = Student("Shikamaru", "CSE")
print('----------------------')
s3.individualInfo()
print('#############################')
s3.totalInfo()
print('============================')


s4 = Student("Deidara", "BBA")
print('----------------------')
s4.individualInfo()
print('#############################')
s4.totalInfo()
