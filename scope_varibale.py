a=20 #Global Variable------
def num1():
    #Priority give to the local variable-------
    # We can change the value of global variable by using global keyword:
    global a
    a= 50
    # a=30 # Local Variable-------
    return a


print("The number is",num1())