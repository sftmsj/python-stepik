figtype = input()
if figtype == 'прямоугольник':
    a = float(input())
    b = float(input())
    print(float(a * b))
elif figtype == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) * 0.5
    print(float((p * (p - a) * (p - b) * (p - c)) ** 0.5))
elif figtype == 'круг':
    r = float(input())
    print(float(3.14 * (r ** 2)))
