b = [input() for i in range(2)]
b.sort()
if b == ['красный', 'синий']:
    print('фиолетовый')
elif b == ['желтый','синий']:
    print('зеленый')
elif b == ['желтый', 'красный']:
    print('оранжевый')
else:
    print('ошибка цвета')