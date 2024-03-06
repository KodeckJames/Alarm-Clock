# IN ORDER TO USE THIS APP, INSTALL PLAYSOUND MODULE AMD REPLACE IT WITH simpleaudio BELOW FOR IT TO WORK

# pip install playsound/pip3 install playsound/python -m pip install playsound/python3 -m pip install playsound-the library module used to play sound
# from playsound import playsound


import simpleaudio as sa
import time

# ANSI 
CLEAR="\033[2J" #clears the entire terminal screen
CLEAR_AND_RETURN="\033[H" #returns the cursor to the home position so that when we print again , we print over what was there before


def alarm(seconds):
    time_elapsed=0
    print(CLEAR)
    while time_elapsed<seconds:
        time.sleep(1)
        time_elapsed+=1

        time_left=seconds-time_elapsed
        minutes_left=time_left//60
        seconds_left=time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")
    sa("Alarm-Fast-A1-www.fesliyanstudios.com.mp3")    

minutes=int(input("How many minutes to wait: "))
seconds=int(input("How many seconds to wait: "))
total_seconds=minutes*60+seconds
alarm(total_seconds)




