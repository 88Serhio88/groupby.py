from random import randint # импортирование функции randint
x = randint(1,8) # функция randint вернет случайное число от 1 до 8
y = randint(1,8)
print(x, y) # вывод пары случайных чисел

if (x + y) % 2 == 1:
    print('YES')
else:
    print('NO')