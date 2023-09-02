time_inp = int(input("to determine the time of day, enter the time"))
if time_inp in range(5, 12):
    print("It's morning now")
    if time_inp in range(12, 18):
        print("The day is now dude")
    if time_inp in range(18, 23):
        print("Evening")
    if time_inp in range(23, 5):
        print("Night, time to sleep")

else:
     print("Error, try again")