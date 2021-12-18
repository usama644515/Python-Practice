from pygame import mixer
import time
mixer.init()
def water():
    mixer.music.load("123.mp3")
    mixer.music.play()
    mixer.music.get_volume()
    userWater=input("Its time to drink the water\nIf you Drank, Please Enter the 'done' to stop this\n")
    if(userWater=="done"):
        mixer.music.stop()


print("Welcome to the Health Managment System\n")
while(True):
    time.sleep(10)
    while(True):
        water()
        break
    close=input("Write 'exit' to close and 'continue' to continue the Program\n")
    if(close=="exit"):
        break
    elif(close=="continue"):
        continue