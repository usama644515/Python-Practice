def factorial(num):
    if(num<=1):
        return 1
    else:
        return num*factorial(num-1) #------Recall the function-------

number=int(input("Enter the number that you want factorial\n"))
print("The Answer of this number is",factorial(number))