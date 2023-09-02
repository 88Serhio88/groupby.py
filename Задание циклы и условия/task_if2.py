#Пользователь вводит целое число. Выведите YES, если это число является четырехзначным, и NO в противном случае.
integer = int(input("enter a four-digit number"))
if integer > 999 and integer < 10000:
    print("you enter the correct value")

else:
    print("something went wrong, try to enter correct number")