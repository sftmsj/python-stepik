a = float(input())
b = float(input())
op = input()
if (op == '/' and b == 0) or (op == 'mod' and b == 0) or (op == 'div' and b == 0):
    print('Деление на 0!')
elif op == '+':
    print(float(a + b))
elif op == '-':
    print(float(a - b))
elif op == '*':
    print(float(a * b))
elif op == '/':
    print(float(a / b))
elif op == 'mod':
    print(float(a % b))
elif op == 'pow':
    print(float(a ** b))
elif op == 'div':
    print(float(a // b))

