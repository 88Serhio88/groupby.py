from datetime import datetime
import time
import random



odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29,
        31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

 #Программа засыпает на 5 секунд

for i in range(5):
    right_this_minutes = datetime.today().minute
    if right_this_minutes in odds:
        whait_time = random.randint(1,60)
        time.sleep(whait_time)
        print("This minutes seems a little odd.")
    else:
        print("Not an odd minute.")

