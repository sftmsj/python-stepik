# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# for i in range(c,d+1):
#     print('\t',i, end='')
# print()
# for j in range(a,b+1):
#     print(j,end='')
#     for i in range(c,d+1):
#         print('\t', j * i, end='')
#     print()


# a, b = (int(i) for i in input().split())
# s = 0
# if a % 2 == 0:
#     a += 1
# for i in range(a, b + 1, 2):
#     s += i
# print(s)
#--------------------------------------------
# a = int(input())
# b = int(input())
# s = 0
# q = 0

# for i in range(a,b+1):
#     if i % 3 == 0:
#         s += i
#         q += 1
# print(s / q)

abc = 'abc'
for i in abc:
    print(i)

print(abc.count('c'))
