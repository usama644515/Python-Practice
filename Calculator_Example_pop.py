import math
def getValue():
        value1=int(input("Enter First Value\n"))
        value2=int(input("Enter Second Value\n"))
        return [value1,value2]
        #-----It can be used in procedure oriented programming---------
        #lst[0]=value1
        #lst[1]=value2
        # return lst
        #-----OR------
        # return [vlaue1,vlaue2]
def scigetValue():
    value=int(input("Enter the Value\n"))
    return value
def SimpleCalculator():
    who=input("Write any one\n+ for Addition\n- for Subtraction\n* for Multiplicaton\n/ for Division\n")
    if(who=="+"):
        val=getValue()#----we can store the return value in val and access this by list indexes------
        print(f"The Sum of these numbers = {val[0]+val[1]}")
    elif(who=="-"):
        val=getValue()
        print(f"The Difference of these numbers = {val[0]-val[1]}")
    elif(who=="*"):
        val=getValue()
        print(f"The Multiplication of these numbers = {val[0]*val[1]}")
    elif(who=="/"):
        val=getValue()
        print(f"The Division of these numbers = {val[0]/val[1]}")
    else:
        print("Invalid Input\n")
def ScientificCalculator():
    who=input("Write any one\nsin for Sin Value\ncos for Cos Value\ntan for Tan Value\n")
        
    if(who=="sin"):
        val=scigetValue()#-------We can store the return value in val----------
        print(f"The Value of Sin ={math.sin(val)}")
    elif(who=="cos"):
        val=scigetValue()
        print(f"The Value of Cos ={math.cos(val)}")
    elif(who=="tan"):
        val=scigetValue()
        print(f"The Value of Tan ={math.tan(val)}")
def Decision():
    decision=int(input("Write 1 for Simple Calculator\nWrite 2 for Scientific Calculator\n"))
    if(decision==1):
        SimpleCalculator()
    elif(decision==2):
        ScientificCalculator()
    else:
        print("Invalid Input\n")


if __name__=='__main__':
    Decision()
    pass