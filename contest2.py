import matplotlib.pyplot as plt


# 1 ----------------------------------------
# def find_root(num):
#     sum = 0
#     p = num
#     while p != sum:
#         p = sum
#         if not num:
#             num = sum
#         sum = 0
#         while num:
#             sum += (num % 10)
#             num //= 10
#     return sum
#
#
# def quicksort(data):
#     if len(data) < 2:
#         return data
#     pivot = data[0]
#     return quicksort([x for x in data if x[1] < pivot[1] or x[1] == pivot[1] and x[0] < pivot[0]]) + [x for x in data if x[1] == pivot[1] and x[0] == pivot[0]] + quicksort(
#         [x for x in data if x[1] > pivot[1] or x[1] == pivot[1] and x[0] > pivot[0]])
#
# inp = input().split()
# data = []
# for j in inp:
#     data.append([int(j), find_root(int(j))])
# for j in quicksort(data):
#     print(j[0], end=" ")


# 2 ----------------------------------------
# data = list(map(int, input().split()))
# print(-1, end=" ")
# for i in range(1, len(data)):
#     num = -1
#     h = data[i]
#     i -= 1
#     while i+1:
#         if data[i] >= h and num < i:
#             num = i
#         i -= 1
#     print(num, end=" ")


# 3 ----------------------------------------
# def cou(i):
#     sum = 0
#     for j in range(i+1, len(data)):
#         if data[i] < data[j][0]:
#             return data[j][1] + 1
#         # if data[i] < data[j][0]:
#         #     sum += 1
#         # elif data[i] == data[j][0]:
#         #     return sum + data[j][1]
#     return sum
#
# data = list(map(int, input().split()))
# i = len(data)
# # data[i-1] = [data[i-1], 0]
# while i:
#     i -= 1
#     data[i] = [data[i], cou(i)]
#
# for x in data:
#     print(x[1], end=" ")


# 4 ----------------------------------------
# def func(hg):
#     inv = 0
#     for i in range(len(hg)):
#         for j in range(i, len(hg)):
#             if hg[j] < hg[i]:
#                 inv += 1
#     return inv
#
#
# def quicksort(data):
#     if len(data) < 2:
#         return data
#     pivot = data[0]
#     return quicksort([x for x in data if x[1] < pivot[1]]) + [x for x in data if x[1] == pivot[1]] + quicksort(
#         [x for x in data if x[1] > pivot[1]])
#
#
# for _ in range(int(input())):
#     g = int(input().split()[1])
#     data = []
#     for _ in range(g):
#         dat = input()
#         data.append([dat, func(dat)])
#     data = quicksort(data)
#     for j in range(g):
#         print(data[j][0])
#     print()


# 5 ----------------------------------------
# def quicksort(data):
#     if len(data) < 2:
#         return data
#     pivot = data[0]
#     return (quicksort([x for x in data if x[2] > pivot[2] or x[2] == pivot[2] and x[0] < pivot[0]]) +
#             [x for x in data if x[2] == pivot[2] and x[0] == pivot[0]] +
#             quicksort([x for x in data if x[2] < pivot[2] or x[2] == pivot[2] and x[0] > pivot[0]]))
#
#
# def sort_string(data):
#     if len(data) < 2:
#         return data
#     pivot = data[0]
#     return sort_string([x for x in data if x < pivot]) + [x for x in data if x == pivot] + sort_string(
#         [x for x in data if x > pivot])
#
#
# inp = input().split()
# data = []
# for j in inp:
#     data.append([j, "".join(sort_string(j))])
# for i in range(len(data)):
#     if len(data[i]) == 3:
#         continue
#     c = 0
#     ind = []
#     for l in range(len(data)):
#         if data[l][1] == data[i][1]:
#             c += 1
#             ind.append(l)
#     for id in ind:
#         data[id] = [data[id][0], data[id][1], c]
# data = quicksort(data)
# print(data)
# for j in data:
#     print(j[0], end=" ")
# 6 ----------------------------------------
# def func(x):
#     return int(x)*2
#
#
# def check_axis():
#     axis = int(sum(x)/len(x))
#     if abs(axis - sum(x)/len(x)) > 10 ** -5:
#         return 0
#     for dot in xy:
#         if dot[0] < axis:
#             if [2*axis - dot[0], dot[1]] not in xy:
#                 return 0
#     return 1
#
# cou = int(input())
# xy = []
# x = []
# y = []
# for _ in range(cou):
#     xy.append(list(map(func, input().split())))
#     x.append(xy[-1][0])
#     y.append(xy[-1][1])
# print(check_axis())
# plt.plot(x, y)
# plt.show()
