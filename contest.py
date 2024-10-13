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
#
#     return current_row[n]


def leven(str_1, str_2):
    m, n = len(str_1), len(str_2)
    table = [[0 for j in range(n)] for i in range(m)]  # m строк, n столбцов
    for i in range(n):
        table[0][i] = i
    for i in range(m):
        table[i][0] = i
    for i in range(1, m):
        for j in range(1, n):
            a = table[i - 1][j] + 1
            b = table[i][j - 1] + 1
            c = table[i - 1][j - 1]
            if str_1[i] != str_2[j]: c += 1
            table[i][j] = min(a, b, c)
    return(table[-1][-1])


# str1, str2 = input().split(" ")
str1 = "onesecondsimpletest"
str2 = "pattern"
str3 = str1[0:len(str2)]
d = 5
s = []
for i in range(0, len(str1) - len(str2) + 1):
    str3 = str1[i:len(str2)+i]
    s.append(leven(str3, str2))
print(s, min(s), s.index(min(s)))
# print(s.index(min(s)), min(s))


