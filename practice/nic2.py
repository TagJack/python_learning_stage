import random
import re


# def solution(number):
#   # Сумма всех чисел в заданном диапозоне кратные 3 и 5.
#     sum = 0
#     for i in range(1, number):
#         if (i % 3 == 0) or (i % 5 == 0):
#             sum += i
# #
#     return print(sum)
#
# solution(6)
# #

# def longest(a1, a2):
#     print("".join(sorted(set(a1+a2))))
#

# def solution(n):
#     return ''.join(sorted(set(a1+a2)))
# a1 = 'loopingisfunbutdangerous'
# a2 = 'lessdangerousthancoding'
# #
# print(longest(a1, a2))
#

##Аккумулирование.

## Вариант лучьше.
# def accum(s):
#     return print("-".join((a*i).title() for i, a in enumerate(s,1)))
#
# print(accum("Nabsccbb"))


### Маскирование.

#### Вариант лучьше.
# def maskify(text):
#     return "#"*(len(text)-4) + text[-4:]

###
# def maskify(s):
#     for i in s:
#         s = s[:-4] + s[-4:].replace(i, "#")
#     return s


# ### Код получьше.
# def narcissistic(value):
#     return value == sum(int(a) ** len(str(value)) for a in str(value))

# print(narcissistic(153))


#### Удаление гласных с комментов троллей.
# def disemvowel(string):
# return print("".join(c for c in string if c.lower() not in "aeiou"))


#### Я мог сделать так.
# def disemvowel(s):
# for i in "aeiouAEIOU":
#     s = s.replace(i,'')
# return s

# print(disemvowel("This website is for losers LOL!"))

## Код по короче.
# def alphabet_position(text):
#     return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
#
# print(alphabet_position("asd"))


#### Функия Рост населения.
# def np_year(p0, percent, aug, p):
#     times = 0
#     while p0 <= p:
#         p0 += int(p0 * (percent / 100)) + aug
#         times += 1
#         if int(p0) >= p:
#             break
#
#     return print(times)


#### Код по короче и с рекурсией.
# def nb_year(p0, percent, aug, p, years = 0):
#     if p0 < p:
#         return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
#     return years
# nb_year(1500, 5, 100, 5000)
# print(num)
#
#### Код разделяет содержимое строки по два элемента.
# import re
#
# def solution(s):
#     return re.findall('..', s + '_')

# print(solution("asdывs"))
#

#### Функция сокращения суммы.
### код легче.
# def digital_root(n):
#     return print(n if n < 10 else digital_root(sum(map(int,str(n)))))

# Доработал
# def digital_root(n):
# num = sum(list(int(i) for i in str(n)))
# if num <= 9: return print(num)
# else: return digital_root(num)


### Consec_string вычисление дxлиннейшей строки

### Нунжно разобраться
# def longest_consec(strarr, k):
#     if (len(strarr) == 0 or k <= 0) or len(strarr) < k:
#         return ""
#     lst = [''.join(strarr[i:i+k]) for i in range(len(strarr))]
#     return max(lst, key=len) #max(lst, key= lambda x: len(x))

# arr = ['morning', 'downtown', 'motley', 'holder', 'teaspoon', 'helicopter', 'water', 'gasket', 'header', 'burning']
# print(longest_consec(arr, 3))


#### Секунды в час минуты и секунды.
# def make_readable(seconds):
#     hours, seconds = divmod(seconds, 60 ** 2)
#     minutes, seconds = divmod(seconds, 60)
#     return print('{:02}:{:02}:{:02}'.format(hours, minutes, seconds))
#


#### Робота со строками
# data = ['Ivan', 32, 'world']
# info = 'Name: {}, Age: {}, Adress: {}'.format(*data)
# print(info)
#
# name = 'Ivan'
# age = 32
# adress = 'World'
# info = f'Name: {name.title()}, Age: {age}, Adress: {adress.title()}.'
# info = 'Name: %s, Age: %s, Adress: %s.' % (name.title(), age, adress.title())
# print(info)


#### Функция возвращает доменное имя.
## Взгляд попрощще:
# def domain_name(url):
# url = url.replace('https://','')
# url = url.replace('http://','')
# url = url.replace('www.','')
# end = url.find('.')
# return print(url[0:end])


#
# def unique_in_order(text):
#     lst = []
#     for i in text:
#         if not lst or i != lst[-1]:
#             lst.append(i)
#     # if i != lst[-1]:
#     #     lst.append(i)
#     return print(lst)
#
#
# print(unique_in_order('aafnfnnpjgr'))
#

#
# def find_nb(m):
##Not smart enough to solve in proper way, so kind of overtake it.
## We're gonna compare my num with m we was given and return i if they're
#     # equal.
#     # If there is no equal one i return -1.
#     num = 0  # The num.
#     for i in range(m):  # This way i find the number kata needs.
#         num += i ** 3  # This is for having smth to compare.
#         if num == m:  # If there is equal one we get number of cubes.
#             return i  # Number of cubes.
#         if num >= m:  # If there is no equal one we return -1.
#             return -1

# print(find_nb(1073))

### Human readable time from given seconds.
# def format_duration(seconds):
#     times = ['year', 'day', 'hour', 'minute', 'second']
#     if seconds == 0:
#         return "now"
#     else:
#         y, s = divmod(seconds, ((3600 * 24) * 365))
#         d, s = divmod(s, (3600 * 24))
#         h, s = divmod(s, 3600)
#         m, s = divmod(s, 60)
#         time = [y, d, h, m, s]
#         readable_time = []
#
#         l = list(zip(time, times))
#         for i in l:
#             t, ts = i
#             if t:  # Не вклучает если значение 0.
#                 t_s = [ts if t == 1 else ts+'s']
#                 readable_str = f'{str(t)+" "+"".join(t_s)}'  # '4 seconds'
#                 readable_time.append(readable_str)  # ["y year/s", "d day/s", ...]
#         if len(readable_time) == 1:
#             return ("".join(readable_time).strip())
#         else:
#             return (", ".join(readable_time[:-1])+" and "+"".join(readable_time[-1])).strip()

# print(format_duration(323565))


# def productFib(prod):
#     """Способ лучше."""
#     a, b = 0, 1
#     while prod > a * b:
#         a, b = b, a + b
#     return print([a, b, prod == a * b])
#
#
# productFib(714)


# def anagrams(word, words):
#     """Поиск Анаграммы и возврат всех из списка words."""
#     [words.remove(a) for a in words[:] if sorted(a) != sorted(word)]
#     return print(words)


# anagrams('racer', ['crazer', 'caers', 'carer', 'racar', 'racer'])

# ### Конкатенация с перебором.
# ints = [3, 2, 6, 4, 2]
# def f(ints, s):
# seen = []
# for item in ints:
#     if s-item in seen:
#         return [s-item, item]
#     elif item not in seen:
#         seen += [item]

# ints = [4, 3, 1, 5, 8]
# print(f(ints, 8))

###Селекционная сортировка.
# def selection_sort(list):
#     indexing_length = range(0, len(list)-1)
#     for i in indexing_length:
#         min = i
#         for j in range(i+1, len(list)):
#             if list[j] < list[min]:
#                 min = j
#         list[i], list[min] = list[min], list[i]
#     return list
#
# list_a = []
# for i in range(100):
#     list_a.append(randint(0, 100))
# print(list_a)
# print(selection_sort(list_a))


#

# ### Метод поиска значения в не сортированном массиве.
# def binary_search(sequence, item):
#     begin_index = 0
#     end_index = len(sequence) - 1
#
#     while begin_index <= end_index:
#         midpoint = begin_index + (end_index - begin_index) // 2
#         mid_value = sequence[midpoint]
#         print(begin_index, mid_value, end_index)
#         if mid_value == item:
#             return midpoint
#
#         elif item < mid_value:
#             end_index = midpoint - 1
#
#         elif item > mid_value:
#             begin_index = midpoint + 1
#
#     return None
#
# sequence_a = list(range(15))
# item_a = 8
#
# print(binary_search(sequence_a, item_a))


###
# def validSolution(board):
#     for x in range(9):
#         arr = [board[y][x] for y in range(9)] # colum
#         arr2 = [board[x][y] for y in range(9)] # row
#         arr3 = [board[i][y] for y in range(((x%3)*3),(((x%3)*3)+3)) for i in range((int(x/3)*3),(int(x/3)*3)+3)]
#         for i in range(9):
#             if arr[i] in arr[(i+1):]: return False
#             if arr2[i] in arr2[(i+1):]: return False
#             if arr3[i] in arr3[(i+1):]: return False
#     return True
#
# print(validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
#             [6, 7, 2, 1, 9, 5, 3, 4, 8],
#             [1, 9, 8, 3, 4, 2, 5, 6, 7],
#             [8, 5, 9, 7, 6, 1, 4, 2, 3],
#             [4, 2, 6, 8, 5, 3, 7, 9, 1],
#             [7, 1, 3, 9, 2, 4, 8, 5, 6],
#             [9, 6, 1, 5, 3, 7, 2, 8, 4],
#             [2, 8, 7, 4, 1, 9, 6, 3, 5],
#             [3, 4, 5, 2, 8, 6, 1, 7, 9]]))
###
### Примерно как product из itertools
# list1 = [1,2,3,4]
# list2 = [6,7,8,9]
# list3 = list(map(lambda x, y: str(x) + str(y), list1, list2))
# print(list3)
# list3 = list(map(lambda i,j: j * i, list1, list2))


# lst = [[1, 2, 4, 5], [9, 5, 3, 2]]
# lst2 = list(map(lambda x, y: str(x) + str(y), lst[0], lst[1]))
# print(lst2)



###Задача 09. Хайку
# def fun(phrase):
#     res = 0
#     for lett in phrase:
#         res += (lett in 'aioue')
#     return res
#
# lst = [
#     'how many gaallon',
#     'of edo s rain did yo',
#     'cuckoooo'
#     ]
#
# print(['NO', 'YES'][[5,7,5] == [fun(phrase) for phrase in lst]])

# print(['No', 'Yes'][[5,7,5] == [len(re.findall(r'[aouie]', phrase)) for phrase in lst]])


####Задача 10. CamelCase -> under_score
string = 'MyVar17 = OtherVar + YetAnother2Var TheAnswerToLifeTheUniverseAndEverything = 42'
# print(re.sub(r'(?<!\b)(?=[A-Z])','_', string).lower())
#
# ## Задача 11. Удаление повторов
# line = 'Довольно распространённая ошибка ошибка — это лишний повтор повтор слова слова. Смешно, не не правда ли? Не нужно портить хор хоровод.'
# # эта регулярка значит "слово, пробел сколько есть, и такое же слово, столько сколько есть.
# # r'\1' - заменяет найденное со
# # впадение единичным экземпляром найденного слова (значение подмаски №1)
# print(re.sub(r'\b(\w+)(\s+\1)+\b', r'\1', line))


## Задача 12. Близкие слова
# line = 'Да он олень, а не заяц!'
# print(re.findall(r'(?<=он).+(?=\W)', line))


### Задача 13. Форматирование больших чисел
# line = '''12 мало
# лучше 123
# 1234 почти
# 12354 хорошо
# стало 123456
# супер 1334567'''

# def repl(m):
#     return str("{:,}".format(int(m[0])))
#
# print(re.sub(r'(\d+)', repl, line))



# ####Задача 14. Разделить текст на предложения.
# line = '''В        этом
# предложении разрывы строки... Но это
# не так важно! Совсем? Да, совсем! И это
#
# не    должно мешать.'''
# # splitted = re.split(r'[.?!:;]', line)
# line = re.sub(r'(\s)(\s+)', r'\1', line)
# for i in re.split(r'(?<=[.?!:…])', line):
#     print(i)


# ####Задача 15. Форматирование номера телефона
# import re
#
# lst = ["+7 123 456-78-90", "8(123)456-78-90", "7(123) 456-78-90", "1234567890", "123456789", "+9 123 456-78-90",
#        "+7 123 456+78=90", "+7(123 45678-90", "8(123  456-78-90"]
#
# # with open('list_of_numbers.txt', 'w') as f:
# #     for i in lst:
# #         f.writelines(i+'\n')
#
# lst2 = []
# with open('list_of_numbers.txt', 'r') as f:
#     for i in f.readlines():
#         lst2.append(i.strip())
#
# for i in lst2:
#     if re.fullmatch(r'(?:\+?[7-8]?[\s\(]?\d{3}\)?\s?\d{3}[\s\-]?\d{2}[\s\-]?\d{2})', i): # Нашол нужное
#         i = i.replace("(","").replace(")","").replace(" ", "").replace("-","").replace("+","") # Убрал все лишнее
#         if i[0] == "8":
#             i = i[0].replace('8','7') + i[1:] # Добавил отсутствующее.
#         if len(i) < 11:
#             i = "7" + i
#         print(f'+{i[0]} {i[1:4]} {i[4:7]}-{i[7:9]}-{i[9:]}') # Форматированный вывод.
#     else:
#         print("Fail.")


# ####Задача 16. Поиск e-mail'ов — 2
# examp = """Иван Иванович!
# Нужен ответ на письмо от ivanoff@ivan-chai.ru.
# Не забудьте поставить в копию
# serge'o-lupin@mail.ru- это важно."""
#
# examp2 = """NO: foo.@ya.ru, foo@.ya.ru, foo@foo@foo
# NO: +foo1@ya.ru, foo2@ya-ru
# NO: foo@ya_ru, -foo3@ya.ru-, foo4@ya.ru+
# NO: foo..foo7@ya.ru
# YES: (boo1@ya.ru), boo2@ya.ru!, boo3@ya.ru"""
#
# print(re.findall(r'(?<![\+-.])[a-z]+?\d?[\'._+-]?[a-z]+?\d?[\'._+-]?[a-z]+\d?@[a-z]+[\'._+-]?[a-z]*?\.[a-z][a-z][a-z]?(?![\+])', examp2))


## Snail sort.
# array = [[1,3,4,5],
#          [6,7,8,9],
#          [1,2,3,4],
#          [2,3,4,5]]
#
# def solution(arr):
#     res = []
#     while len(arr) > 1:
#         res = res + arr.pop(0)
#         res = res + [row.pop(-1) for row in arr]
#         res = res + list(reversed(arr.pop(-1)))
#         res = res + [row.pop(0) for row in arr[::-1]]
#     return res if not arr else res + arr(0)
#
# print(solution(array))