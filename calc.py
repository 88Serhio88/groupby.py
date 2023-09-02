# Калькулятор (рабочий)
#If - условие, elif - если первое условие выполняется, второе не будет выполняться, ставится под вторым
# else - если ни одно условие не совпало то можно сделать вывод сообщения например: "Выбрана не верная операция"
# use Colorama to make Termcolor work on Windows too
# для превращения файла в exe, команда в cmd - pyinstaller test.py и далее   название файла пример test.py


from colorama import init
from colorama import Fore, Back, Style

print(Back. WHITE)
print(Fore.BLACK)


s = input("Знак (+,-, *, /):")

print(Back. YELLOW)

a = float(input("a = "))
print(Back. CYAN)

b = float(input("b = "))

print(Back. RED)

if s == "+":
	print(a + b)
elif s == "-":
	print(a - b)
elif s == "*":
	print(a * b)
elif s == "/":
	if b != 0:
		print(a / b)
	else:
		print("Деление на ноль")

input()