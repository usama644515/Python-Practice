class Employee:
    company="Google"
    def __init__(self,name,position):
        self.name=name
        self.position=position
    def display(self):
        print(f"Your Name is {self.name} \nYour position in comapny is {self.position}")
    
class Salary(Employee):
        def __intit__(self,salary):
            self.salary=salary
        #-----Static Method can be used when we dont use "self" Keyword as a argument-------
        # @staticmethod
        def displaySalary(self):
            print(f"Your Salary = RS.{self.salary}")

usama=Salary("Usama","Programmer")
usama.salary=45000
usama.display()
usama.displaySalary()    