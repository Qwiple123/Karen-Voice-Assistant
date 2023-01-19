import os
import time

os.system('cls')
width = 120
height = 30
strings = ['*' * width, '-' * width]
while True:
    print((strings[0]+strings[1])*15)
    time.sleep(0.3)
    # os.system('cls')
    
    print((strings[1]+strings[0])*15)
    time.sleep(0.4)
    os.system('cls')
    
