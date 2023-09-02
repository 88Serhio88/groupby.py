day_inp = int(input("Enter the day of the week from 1 to 7"))
if day_inp in range(1,6):
    print("working day")
elif day_inp in range(6,8):
    print("weekend")
else:
    print("Something went wrong, look the conditions")