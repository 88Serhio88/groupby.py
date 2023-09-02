# del - удаление переменной (пример del number)
#number = 5 # int - целое число
#digit = 4.33443 # float - вещественное значение
#word = "Результат:" # string - строка
#boolean = True # bool - булевая переменная
#print (word + str(digit))
#str_num =  "10" # string
#print (word + str (number + int (str_num)))
#number = 7
#print ("Результат:", number)

num1 = int (input ("Введите первое число:"))

num2 = int (input ("Введите второе число:"))

num1 -= 5

print ("Результат:", num1+num2)
print ("Результат:", num1-num2)
print ("Результат:", num1*num2)
print ("Результат:", num1/num2)
print ("Результат:", num1**num2)
print ("Результат:", num1//num2)

word = "Hi"
print(word * 5)