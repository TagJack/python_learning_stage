import random
import decimal

# ### Конкатенация с перебором.
# ints = [2, 4, 8, 4, 6, 1]
#
# def fun(ints, s):
#     seen = []
#     for item in ints:
#         if s-item in seen:
#             return print([s-item, item])
#         elif item not in seen:
#             seen += [item]
#
# fun(ints, 8)

# ##Селекционная сортировка.
# def selection_sort(arr):
#     indexing_length = range(0, len(arr))
#     for i in indexing_length:
#         min = i
#         for j in range(i+1, len(arr)-1):
#             if arr[j] < arr[min]:
#                 min = j
#         arr[i], arr[min] = arr[min], arr[i]
#
#     return arr
#
# n = 100
# list_a = []
# for i in range(0, n):
#     list_a.append(randint(1, 99))
# print(list_a)
# print(selection_sort(list_a))

# ### Метод поиска значения в не сортированном массиве.
# def binary_search(sequence, item):
#     begin, end = 0, len(sequence) - 1
#     while begin <= end:
#         print(begin, end)
#         midpoint = begin + (end - begin) // 2
#         mid_value = sequence[midpoint]
#         if item == mid_value: return midpoint
#         elif item < mid_value: end = midpoint - 1
#         elif item > mid_value: begin = midpoint + 1
#     return None
#
# arr = list(range(0,15))
# print(binary_search(arr, 8))

# """Есть N коробок, некий человек последовательно проходит и закрывает
# куждую вторую коробку. Затем снова проходит уже по каждой третьей коробку
# и , если она открыта - закрывает, если уже закрыта - открывает. Потом
# повторяет цикл по каждой 4-ой и так до N."""
# def f(n):
#     lst = []
#     for i in range(n): lst.append(0)
#     check = 1
#     leap = 2
#     while not leap == n+1:
#         if lst[check] == 0: lst[check] = 1
#         else: lst[check] = 0
#         check += leap
#         if check > n:
#             check = leap
#             leap += 1
#     return lst
# print(f(10))


## Алгоритм выявления самого повторяемого слова и самого длинного слова в предложении.
# text = 'this is random text in random place with random words nothing has sense here.'

# def solution(text):
#     t_dict = {}
#     t_list = text.split()
#     longest = max(t_list, key=len)
#     for i in range(len(t_list)):
#         t_dict[t_list[i]] = text.count(t_list[i])
#     return max(t_dict, key=t_dict.get), longest
#
# print(solution(text))

# def solution(n):
#     numbers = list(range(n))
#     for item in numbers:
#         if (item % 3 == 0) and (item % 5 == 0):
#             item = "FizzBuzz"
#         elif item % 3 == 0 and not (item % 5 == 0):
#             item = "Fizz"
#         elif item % 5 == 0 and not (item % 3 == 0):
#             item = "Buzz"
#         print(item)
#
# solution(100)
#

## Перебор цифр с плавающей точкой.
# def float_range(start, stop, step):
#     while start < stop:
#         yield float(start)
#         start += decimal.Decimal(step)
# #
#     return start
# #
# arr = list(float_range(1, 6, 1.5))
# print(arr)
# print(list(float_range(1, 10, '0.5')))

## Разварачивает строку
# text = 'this is random text in random place with random words nothing has sense here.'
# def reverse(text):
#     return text[::-1].lower()

text = 'this is random text in random place with random words nothing has sense in here.'

# def solution(text):
#     t_list = text.split()
#     t_dict = {}
#     longest = max(t_list, key=len)
#     for i in t_list:
#         t_dict[i] = t_list.count(i)
#     return max(t_dict, key = t_dict.get), longest
#
# print(solution(text))


# def qsort(arr):
#     if len(arr) < 2:
#         return arr
#     else:
#         pivot = arr[0]
#         less = [i for i in arr[1:] if i <= pivot]
#         greater = [i for i in arr[1:] if i > pivot]
#         return qsort(less)+[pivot]+qsort(greater)


def qsort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        more = [i for i in arr[1:] if i >= pivot]
        return qsort(less)+[pivot]+qsort(more)

arr = list(range(10, 1000, 10))
random.shuffle(arr)
print(arr)
print(qsort(arr))