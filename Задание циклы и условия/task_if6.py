number = int(input("Enter the number"))
sign = input("positive or negative sign of a number")
if number == 0:
    print("Zero")
    exit()
if number % 2 == 0:
    print(sign, "even")
else:
    print(sign, "odd")