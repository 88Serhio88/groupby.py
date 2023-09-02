# for i in range(1, 6, 2):  # range - диапазон
#     print(i)

# count = 0
# word = "Hello World!"
# for i in word:
#     if i == "!":
#         count += 1
#         print("Count:", count)

# i = 5
# while i <= 15001:
# print(i)
#     i += 2

# isHasCar = True
#
# while isHasCar:
#     if input("Введите информацию\n") == "Stop":
#         isHasCar = False

# for i in range(1, 11):
#     if i == 5:
#         break  # оператор выходит из цикла
#
#     if i % 2 == 0:
#         continue
#
#     print(i)

found = None
for i in "hello":
    if i == "l":
        found = True
        break
else:
    found = False
print(found)

