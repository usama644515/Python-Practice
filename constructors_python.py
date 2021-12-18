class Employee:
    @staticmethod #-----Static method or function run without arguments---------
    def wish():
        print("Have a Nice Day\n")
    def __init__(self,name,salary,jobTitle):
        self.name=name
        self.salary=salary
        self.jobTitle=jobTitle
    def display(self):
        print(f"Your Name is {self.name}")
        print(f"Your Salary is {self.salary}")
        print(f"Your Job Title is {self.jobTitle}")

    pass   

if __name__ =='__main__':
    name=input("Enter Your Name\n")
    salary=int(input("Enter Your Salary\n"))
    jobTitle=input("Enter Your Job Title\n")
    usama=Employee(name,salary,jobTitle)#---constructor take these arguments and run when object is created---
    usama.display()
    pass



