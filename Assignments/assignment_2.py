
num=int(input("Enter Your Percentage\n"))
# num=79
if (num<=100 and num>=80):
    print("Your Grade is A+\n")
elif (num<80 and num>=70):
    print("Your Grade is A\n")
elif (num<70 and num>=60):
    print("Your Grade is B\n")
elif (num<60 and num>=50):
    print("Your Grade is C\n")
elif (num<50 and num>=33):
    print("Your Grade is D\n")
elif (num<33 and num>=0):
    print("You Fail\n")
else:
    print("Please Enter Valid Percentage\n")
       
