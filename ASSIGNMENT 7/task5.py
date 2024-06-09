class Employee:
    def __init__(self, name, id , dep ):
        self.name = name
        self.id = id
        self.dep = dep
        self.selary = 30000
    def employeeDetails(self):
        print(f"Name: {self.name}, dept: {self.dep}\
                \nEmployee Id: {self.id}, Selary: {self.selary}")

    def workDistribution(self , a ):
        if a == "Human Resource":
            print("Collect work distribution details from the manager.")
        else:
            print("Collect work distribution details from the HR department.")
    
    def increment(self):
        self.selary += self.selary * .1
class Foreign_employee(Employee):
    def __init__(self, name, id , dep):
        super().__init__(name, id , dep)
        self.type = "Foreign"
    def employeeDetails(self):
        print(f"Name: {self.name}, dept: {self.dep}\
                \nEmployee Id: {self.id}, Selary: {self.selary}\
                    \nEmployee Type: {self.type}")
    def increment(self):
        self.selary += self.selary * .15    
        
class Part_time_employee(Employee):
    def __init__(self, name, id, dep):
        super().__init__(name, id, dep)
        self.selary = 15000
        self.type = "Part Time"
    def employeeDetails(self):
        print(f"Name: {self.name}, dept: {self.dep}\
                \nEmployee Id: {self.id}, Selary: {self.selary}\
                    \nEmployee Type: {self.type}")
    def increment(self):
        print("No increment for part time employee")      
        
    
print("1------------------------------------------")
emp1=Employee("Nawaz Ali", 102, "Marketing")
print("2------------------------------------------")
emp1.employeeDetails()
print("3------------------------------------------")
emp1.workDistribution("Marketing")
print("4------------------------------------------")
emp1.increment()
emp1.employeeDetails()
print("5------------------------------------------")
f_emp=Foreign_employee("Nadvi", 311, "Human Resource")
f_emp.employeeDetails()
print("6------------------------------------------")
f_emp.workDistribution("Human Resource")
print("7------------------------------------------")
f_emp.increment()
f_emp.employeeDetails()
print("8------------------------------------------")
p1_emp=Part_time_employee("Asif", 210, "Sales")
p2_emp=Part_time_employee("Olive", 223, "Accounts")
print("9------------------------------------------")
p1_emp.employeeDetails()
print("10------------------------------------------")
p1_emp.workDistribution("Sales")
print("11------------------------------------------")
p2_emp.increment()
print("12------------------------------------------")
p2_emp.employeeDetails()

