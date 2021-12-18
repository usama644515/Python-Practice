
# def number(*args):
#     print(args[0])

# lst=["usama","Haris","Mudasir"] #----It can print only 0 index value------
# number(*lst)
#________________________________________________________________________________________

# def number2(normal,*args): #---We can use normal arguemnt and *args both in it-----
#     print(normal)
#     for item in args:
#         print(item)

# num="This is the list"
# lst=["usama","Haris","Mudasir"]
# number2(num,*lst)
#________________________________________________________________________________________

def number3 (normal ,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(f"{key} is a {value}") #-------F String (String Formatting)---------


var="This is the list"
lst=["usama","Haris","Mudasir"] 
keyValue={"Usama":"Programmer","Mudasir":"Engineer","Saad":"Programmer"} #-----We use Dictionary------
number3(var,*lst,**keyValue)