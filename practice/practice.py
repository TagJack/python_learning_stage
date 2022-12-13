import random

# class SortSearch():
#     def __init__(self, arr):
#         self.arr = arr
#
#
#     def sort(self):
#         indexing = list(range(0, len(self.arr)))
#         for i in indexing:
#             min = i
#             for n in range(i+1, len(indexing)):
#                 if self.arr[n] < self.arr[min]:
#                     min = n
#             self.arr[min], self.arr[i] = self.arr[i], self.arr[min]
#         return self.arr
#
#
#     def search(self, item):
#         self.sorted_arr = self.sort()
#         begin, end = 0, len(self.sorted_arr) - 1
#         while begin <= end:
#             mid_point = begin + (end - begin) // 2
#             midvalue = self.sorted_arr[mid_point]
#             print(begin, mid_point, end)
#             if midvalue == item: return mid_point
#             elif item < midvalue: end = mid_point - 1
#             elif item > midvalue: begin = mid_point + 1
#         return None
#
# array = list(range(150))
# random.shuffle(array)
#
# num = SortSearch(array)
# print(num.search(88))



def find_smollest(arr):
    smallest = arr[0]
    smallest_ind = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_ind = i
    return smallest_ind

def sort(arr):
    lst = []
    for i in range(len(arr)):
         smallest = find_smollest(arr)
         lst.append(arr.pop(smallest))
    return lst

array = list(range(10000 ))
random.shuffle(array)

print(sort(array))
pri

