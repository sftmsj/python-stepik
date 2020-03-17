# s = 'abc'
# s.upper()
# s.lower()
# s.find('P') # вывод -1 - не входит 
# s.replace('c', 'C')
# s.count(p)
# if 'ab' in s:
#     print('ok')

# st = input()
# ust = st.upper()

#посчитать кол-во вхождений
#genome = input()
#print(genome.count('C'))

#Задача на G C
# a = 'G'
# b = 'C'

# c = ust.count(a)
# d = ust.count(b)
# e = len(ust)

# gc = (c + d) / e * 100
# print(gc)

#Вывод определённых последовательностей из строки
# dna = 'abcdefgh'
# dna[1] второй символ
# dna[1:4] со первого по третий включительно
# dna[:4] до третьего
# dna[4:] с четвертого до конца
# dna[-4:] последние четыре 
# dna[1:-1] с первого до предпоследнего
# dna[1:-1:2] с начала до предпоследнего через один 
# dna[::-1] в обратном порядке

#Упражнение на вывод
# s = 'abcdefghijk'
# print(s[3:6])
# print(s[:6])
# print(s[3:])
# print(s[::-1])
# print(s[-3:])
# print(s[:-6])
# print(s[-1:-10:-2])
#Упражнение на нахождение зеркальных слов (палиндромов)
# s = input()
# r = s[::-1]
# if s == r:
#     print('yes')
# else:
#     print('no')

#Упражнение на замену кол-ва букв на цифры
# inpstr = input()
# resstr = inpstr

# cnt = 1
# length = len(inpstr)

# for i in range(len(inpstr)-1):
#     a = resstr[i]
#     b = resstr[i + 1]
#     if a.isdigit() == True:
#         continue
#     else:
#         if a == b:
#             cnt += 1
#         else:
#             if cnt == 1:
#                 resstr = resstr.replace(resstr[i],resstr[i] + '1')
#             else:
#                 resstr = resstr.replace(resstr[i + 1 - cnt : i + 1], a+str(cnt))
#             cnt = 1
# if inpstr == resstr:
#     resstr = resstr.replace(resstr[1:], a+str(cnt))
# else:
#     resstr = resstr.replace(resstr[i], str(cnt))          
# print(resstr)
#ПОЛУЧИЛСЯ ФАИЛ



# dnc = input()
# dnc2 = ""
# i=1
# j=1
# while i <= len(dnc):
#     count = 1
#     while (i<=len(dnc)-1) and (dnc[i] == dnc[i-1]):
#         count = count + 1
#         i+=1
#     dnc2 = dnc2 + dnc[i-1] + str(count)
#     i+=1
# print(dnc2) 

t=()
print(t)