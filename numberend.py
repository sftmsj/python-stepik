# q = int(input())
# if (q % 10 == 0) or (q % 5 == 0) or (q % 6 == 0) or ((q % 7 == 0)) or (q % 8 == 0) or (q % 9 == 0):
#     name = 'программистов'
# elif (q >= 11 and q <= 14) or ((q >= 111 and q <= 114)) or ((q >= 211 and q <= 214)) or ((q >= 311 and q <= 314)) or ((q >= 411 and q <= 414)) or ((q >= 511 and q <= 514)) or ((q >= 611 and q <= 614)) ((q >= 711 and q <= 714)) or ((q >= 811 and q <= 814)) ((q >= 911 and q <= 914)):
#     name = 'программистов'
# elif (q % 2 == 0) or (q % 3 == 0) or (q % 4 == 0):
#     name = 'программиста'
# else:
#     name = 'программист'
# print(name)

tp = int(input('Введите число: '))

if tp < 0:
    print('Ошибка, введите положительное число')
elif tp % 10 == 1 and tp % 100 != 11: # Формула 1
    print(tp, 'программист')
elif tp % 10 >= 2 and tp % 10 <= 4 and (tp % 100 < 10 or tp % 100 > 20): # Формула 2
    print(tp, 'программиста')
else:
    print(tp, 'программистов')