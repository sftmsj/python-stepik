# a = 5
# while a <= 55:
#     print(a, end=' ')
#     a += 2

# c = 1
# while c < 7:
#     print('*' * c)
#     c += 1

# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1

# a = int(input())
# s = 0
# while a != 0:
#     s += a
#     a = int(input())
# print(s)

# a = int(input())
# b = int(input())
# n = 1
# while n <= a * b:
#     if (n % a == 0) and (n % b == 0):
#         break
#     else:
#         n += 1
# print(n)

# a = int(input())
# b = int(input())
# d=a
# while d%b!=0:
#     d+=a
# print(d)

# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         continue
#     i = i + 1
# print(i)

a = int(input())
while a < 100:
    if a > 10:
        print('output', a)
    else:
        a = int(input())
        continue
    a = int(input()) 


