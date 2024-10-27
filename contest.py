# 1 -------------------------
# n, m = input().split()
# n, m = int(n), int(m) # строки, столбцы
# table = [[0 for j in range(m)] for i in range(n)]
# table[0][0] = 1
# # for i in range(n):
# #     print(*table[i])
#
# for i in range(1, n):
#     for j in range(1, m):
#         a, b = 0, 0
#         if i >= 2:
#             a = table[i - 2][j - 1]
#         if j >= 2:
#             b = table[i - 1][j - 2]
#         table[i][j] = a + b
# # for i in range(n):
# #     print(*table[i])
# print(table[-1][-1])

# 2 ----1--2--3--------------
# n = int(input())
# nums = [0, 1, 1]
# act = [] # 1, 2, 3 - -1, *2, *3
# trace = [n]
# for i in range(4, n+1):
#     if i % 3 == 0:
#         a = nums[i // 3 - 1]
#     else:
#         a = float("inf")
#     if i % 2 == 0:
#         b = nums[i // 2 - 1]
#     else:
#         b = float("inf")
#     c = nums[i - 2]
#     nums.append(min(a, b, c) + 1)
# print(nums[n-1])
# # print(nums)
#
# l = n
# while l != 1:
#     if l % 3 == 0:
#         a = nums[l // 3 - 1]
#     else:
#         a = float("inf")
#     if l % 2 == 0:
#         b = nums[l // 2 - 1]
#     else:
#         b = float("inf")
#     c = nums[l - 2]
#     e = min(a, b, c)
#     if e == c:
#         act.append(1)
#     elif e == b:
#         act.append(2)
#     else:
#         act.append(3)
#
#     if act[-1] == 3:
#         l //= 3
#     elif act[-1] == 2:
#         l //= 2
#     elif act[-1] == 1:
#         l -= 1
#     trace.append(l)
#
# for i in trace[::-1]:
#     print(i, end = " ")

# 3 -----------------------------------
# n = int(input())
# nums = input().split(" ")
# for i in range(n):
#     nums[i] = int(nums[i])
# s = sum(nums)
# if s % 3:
#     print(0)


# 4 -----------------------------------
# def levenstein(str_1, str_2):  # from habr
#     n, m = len(str_1), len(str_2)
#     if n > m:
#         str_1, str_2 = str_2, str_1
#         n, m = m, n
#
#     current_row = range(n + 1)
#     for i in range(1, m + 1):
#         previous_row, current_row = current_row, [i] + [0] * n
#         for j in range(1, n + 1):
#             add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
#             if str_1[j - 1] != str_2[i - 1]:
#                 change += 1
#             current_row[j] = min(add, delete, change)
#     return current_row[n]


# def leven(str_1, str_2):
#     m, n = len(str_1), len(str_2)
#     table = [[0 for j in range(n + 1)] for i in range(m + 1)]  # m строк, n столбцов
#     for i in range(n + 1):
#         table[0][i] = i
#     for i in range(m + 1):
#         table[i][0] = i
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             a = table[i - 1][j] + 1
#             b = table[i][j - 1] + 1
#             c = table[i - 1][j - 1]
#             if str_1[i - 1] != str_2[j - 1]: c += 1
#             table[i][j] = min(a, b, c)
#     return(table[-1][-1])
#
#
# str1, str2, d = input(), input(), int(input())
# # str1 = "onesecondsimpletest"
# # str2 = "pattern"
# # d = 4
# f = 0
# for length in range(1, len(str2)):
#     for i in range(0, len(str1) - length):
#         for j in range(len(str2) - length + 1):
#             str3 = str1[i:i + length]
#             str3 = ' '*j + str3
#             if leven(str2, str3) <= d:
#                 if(f == 0):
#                     f = 1
#                     print(i, length)
#                 break


# 5 -----------------------------------------------
# n, m = input().split() # строк, столбцов
# n, m = int(n), int(m)
# dat = []
# max_size = 1
# seq = 0
# vert_seq = 0
# hei = []
# # def show():
# #     for i in range(n):
# #         print(*dat[i])
#
#
# for i in range(n):
#     dat.append(list(map(int, input().split())))
#
# for i in range(n):
#     for j in range(m):
#         if dat[i][j]:
#             seq += 1
#         if dat[i][j] != 1 or j == m-1: # при окончании строки или достаточно длинной последовательности 1
#             if seq > max_size:
#                 for k in range(j - seq + 1, j + 1):
#                     for t in range(i, n):
#                         if dat[t][k]:
#                             vert_seq += 1
#                         else:
#                             break
#                     hei.append(vert_seq)
#                     vert_seq = 0
#                 # выше - создание списка с количеством непрерывных стобцов 1 вниз от взятой строки
#                 # print(hei)
#                 # далее - нахождение максимальной последовательности длиной n стобцов > n
#
#                 max_seq = 1
#                 c = 0
#                 for g in range(2, seq):
#                     for l in hei:
#                         if l >= g:
#                             c += 1
#                         else:
#                             if c >= g:
#                                 max_seq = max(max_seq, c)
#                             c = 0
#                     if c >= g:
#                         max_seq = max(max_seq, c)
#                     c = 0
#                 hei = []
#                 max_size = max(max_size, max_seq)
#             seq = 0
#
#
# print(max_size)
# 6 -----------------------------------------------
# string = "1+2-3*4+5"
# data = [string[i] for i in range(len(string))]
#
# def c(data, state=1):
#     if len(data) == 1:
#         return int(data[0])
#     elif len(data) == 3:
#         if data[1] == "+":
#             return int(data[0]) + int(data[2])
#         elif data[1] == "-":
#             return int(data[0]) - int(data[2])
#         elif data[1] == "*":
#             return int(data[0]) * int(data[2])
#     else:
#         value_max = -float("inf")
#         value_min = float("inf")
#         for i in range(0, len(data) // 2):
#             prev = data[0:2*i + 1]
#             after = data[2 * i + 2:]
#
#             if data[2*i+1] == "*":
#                 value_max = max(c(prev) * c(after), value_max)
#                 value_min = min(c(prev) * c(after), value_min)
#             elif data[2*i+1] == "-":
#                 value_max = max(c(prev) - c(after), value_max)
#                 value_min = min(c(prev) - c(after), value_min)
#             elif data[2*i+1] == "+":
#                 value_max = max(c(prev) + c(after), value_max)
#                 value_min = min(c(prev) + c(after), value_min)
#             print(prev, data[2*i + 1], after, value_min, value_max)
#         if state:
#             return value_max
#         else:
#             return value_min
#
# print(c(data))