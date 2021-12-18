import random
import time
lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
chance=10
print("Welcome to the Game\nChoose the Number between 1 to 20\n")
for i in range(0,10):
# while(chance>=1):
    chance-=1
    computer=random.choice(lst)
    user=int(input("Enter the Number\n"))
    if(user==computer):
        print(f"You Win at left {chance} Chances,You Choose {user} and computer choose {computer}\n")
        break
    elif(user>20):
        print(f"Invalid Number, Your left chances = {chance}, You Choose {user} and Computer choose {computer}")
        continue
    elif(user<1):
        print(f"Invalid Number, Your left chances = {chance}, You Choose {user} and Computer choose {computer}")
        continue
    elif(chance==0):
        print(f"Your chances = {chance}, You Choose {user} and Computer choose {computer}")
    else:
        print(f"Try Agin Your left chances = {chance}, You Choose {user} and Computer choose {computer}")
        continue
if(chance==0):
    time.sleep(1)
    print("Game Over")

    

