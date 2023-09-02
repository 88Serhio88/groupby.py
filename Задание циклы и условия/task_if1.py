# Пользователь вводит два целых числа. Выведите меньшее из них.
first_int = int(input("enter the first integer"))
second_int = int(input("enter the second integer"))
if first_int < second_int:
    print(first_int, "the first number is less than the second")
else:
    print(second_int,"the second number is less than the first")