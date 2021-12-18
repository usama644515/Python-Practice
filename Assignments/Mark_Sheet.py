
print("\n")
# isl=int(input("Enter your islamiat Marks\n"))
# maths=int(input("Enter your Maths Marks\n"))
# english=int(input("Enter your English Marks\n"))
isl=80
maths=75
english=80
add=isl+maths+english
total=300
percent=100
percentage=add*percent/total
print("Total Marks =",total,"\nYour Obtain marks =",add)
print("Your Percentage is","%.2f"%percentage,"%")
# print("Your Percentage is",round(percentage,2),"%") #----Round function can be used for round off the float----
# c=int(percentage)
if (percentage<=100 and percentage>=80):
    print("Your Grade is A+\n")
elif (percentage<80 and percentage>=70):
    print("Your Grade is A\n")
elif (percentage<70 and percentage>=60):
    print("Your Grade is B\n")
elif (percentage<60 and percentage>=50):
    print("Your Grade is C\n")
elif (percentage<50 and percentage>=33):
    print("Your Grade is D\n")
elif (percentage<33 and percentage>=0):
    print("You Fail\n")
else:
    print("Please Enter Valid Percentage\n")

# print ("%.2f" % 12.34567) ----It can used for round off the foat value----