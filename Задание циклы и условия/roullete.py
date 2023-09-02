num = int(input())
if num == 0:
    print("зеленый")
elif num % 2 == 0 and 1 <= num <= 10 or num % 2 == 0 and 19 <= num <= 28:
    print("черный")
elif 1 <= num <= 10 or 19 <= num <= 28:
    print("красный")
elif num % 2 == 0 and 11 <= num <= 18 or num % 2 == 0 and 29 <= num <= 36:
    print("красный")
elif 11 <= num <= 18 or 29 <= num <= 36:
    print("черный")
else:
    print("ошибка ввода")