import math
class calculator:
    def getValue(self):
        self.value1=int(input("Enter First Value\n"))
        self.value2=int(input("Enter Second Value\n"))
        
    def scigetValue(self):
        self.value=int(input("Enter the Value\n"))
    def SimpleCalculator(self):
        who=input("Write any one\n+ for Addition\n- for Subtraction\n* for Multiplicaton\n/ for Division\n")
        if(who=="+"):
            self.getValue()#{lst[0]+lst[1]}
            print(f"The Sum of these numbers = {self.value1+self.value2}")
        elif(who=="-"):
            self.getValue()
            print(f"The Difference of these numbers = {self.value1-self.value2}")
        elif(who=="*"):
            self.getValue()
            print(f"The Multiplication of these numbers = {self.value1*self.value2}")
        elif(who=="/"):
            self.getValue()
            print(f"The Division of these numbers = {self.value1/self.value2}")
        else:
            print("Invalid Input\n")
        pass
    def ScientificCalculator(self):
        who=input("Write any one\nsin for Sin Value\ncos for Cos Value\ntan for Tan Value\n")
        
        if(who=="sin"):
            self.scigetValue()
            print(f"The Value of Sin ={math.sin(self.value)}")
        elif(who=="cos"):
            self.scigetValue()
            print(f"The Value of Cos ={math.cos(self.value)}")
        elif(who=="tan"):
            self.scigetValue()
            print(f"The Value of Tan ={math.tan(self.value)}")
        pass
    def Decision(self):
        decision=int(input("Write 1 for Simple Calculator\nWrite 2 for Scientific Calculator\n"))
        if(decision==1):
            self.SimpleCalculator()
        elif(decision==2):
            self.ScientificCalculator()
        else:
            print("Invalid Input\n")
 
if __name__ =='__main__':
    user=calculator()
    user.Decision()
    pass