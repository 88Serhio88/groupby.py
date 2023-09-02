a, b, op = input(), input(), input()
if op not in ('+', '-', '*', '/'):
    print("Неверная операция")
else:
    print("На ноль делить нельзя!" if op == '/' and b == '0' else eval(a + op + b))