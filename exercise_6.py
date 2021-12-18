import random
num=0
win1=0 #-----User-------
win2=0 #-----computer------
while(num<10):
# for i in range(0,10):
    lst=["Snake","Water","Gun"]
    a=random.choice(lst) #--We use random choice function for radom vlaues----=
    print("s for snake\nw for water\ng for gun")
    user=input("Enter the Word\n")
    print("Computer Choose",a)
    if(a=="Snake" and user=="s"):
        print("This is tie\n")
    elif(a=="Snake" and user=="w"):
        print("You Loose\n")
        win2=win2+1
    elif(a=="Snake" and user=="g"):
        print("You Win\n")
        win1=win1+1
    elif(a=="Water"and user=="s"):
        print("You Win\n")
        win1=win1+1
    elif(a=="Water"and user=="w"):
        print("This is tie\n")
    elif(a=="Water"and user=="g"):
        print("You Loose\n")
        win2=win2+1
    elif(a=="Gun"and user=="s"):
        print("You Loose\n")
        win2=win2+1
    elif(a=="Gun"and user=="w"):
        print("You Win\n")
        win1=win1+1
    elif(a=="Gun"and user=="g"):
        print("This is tie\n")
    num=num+1
if(win1>win2):
    print("You Win\n")
    print("Your Correct Answer is",win1,"\nComputer Correct Answer is",win2)
elif(win1==win2):
    print("This game is tie\n")
    print("Your Correct Answer is",win1,"\nComputer Correct Answer is",win2)
else:
    print("You lose\n")
    print("Your Correct Answer is",win1,"\nComputer Correct Answer is",win2)

