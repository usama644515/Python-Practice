import time

# def function1(value):
#     intial=time.time()
#     for i in range(10):
#         print(value)
#     print("After the exectuion of for loop",time.time()-intial,"Second")

# def function2(value):
#     intial=time.time()
#     i=0
#     while(i<10):
#         print(value)
#         i+=1
#     print("After the exectuion of for loop",time.time()-intial,"Second")  

# value=input("Enter some words\n")
# function1(value)
# function2(value)
#_______________________________________________________________________________________________

def function1(value):
    
    for i in range(10):
        print(value)
        time.sleep(2)

def function2(value):
    
    i=0
    while(i<10):
        print(value)
        i+=1
        time.sleep(2)

value=input("Enter some words\n")
function1(value)
function2(value)