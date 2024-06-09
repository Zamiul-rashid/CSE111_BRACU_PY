class Student:
  Id = 0
  def __init__(self, name, department, age, cgpa):
    self.name = name
    self.department = department
    self.age = int(age)
    self.cgpa = float(cgpa)
    Student.Id+=1
    self.id = Student.Id


  def showDetails(self):
    print(f"ID: {self.id}\
            \nName: {self.name}\
            \nDepartment: {self.department}\
            \nAge: {self.age}\
            \nCGPA: {self.cgpa}")

  @classmethod
  def from_String(Cls, info_str):
    return Student(*info_str.split("-"))




s1 = Student("Samin", "CSE", 21, 3.91)
s1.showDetails()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.showDetails()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.showDetails()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.showDetails()


# Write the answer of subtask 5 here
print('A class variable is shared among all instances of a class and stores data that is common to the entire class. It\'s defined outside of any methods in the class and is accessed using the class name or instances of the class. However, instance variables are specific to every object created from the class. They are defined in the class constructor using the "self" keyword and cannot be accessed without an instace. Instance variables are accessed using the instance name.')

# Write the answer of subtask 6 here
print('An instance method takes "self" as the first argument and requires an instance of the class to be called. However, a class method takes the class as the first argument and does not necessarily require an instance of the class to be called.')

