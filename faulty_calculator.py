#                  -------------------------Faulty Calculator------------------------

a=input("Write the symbol in below:\n+ for Addition\n- for Subtraction\n* for Multiplication\n/ for Division\n")
if a=="+":
    num1=int(input("Enter First Value\n"))
    num2=int(input("Enter Second Value\n"))
    if num1==10 and num2==20:
        print("1245")
    else:
        print(num1+num2)    
elif a=="-":
    num1=int(input("Enter First Value\n"))
    num2=int(input("Enter Second Value\n"))       
    if num1==10 and num2==20:
        print("1245")
    else:
        print(num1-num2)
elif a=="*":
    num1=int(input("Enter First Value\n"))
    num2=int(input("Enter Second Value\n"))       
    if num1==10 and num2==20:
        print("1245")
    else:
        print(num1*num2)
elif a=="/":
    num1=int(input("Enter First Value\n"))
    num2=int(input("Enter Second Value\n"))       
    if num1==10 and num2==20:
        print("1245")
    else:
        print(num1/num2)
