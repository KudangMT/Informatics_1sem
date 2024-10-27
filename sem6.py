# 253
# year = int(input())
# print((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)))

# 295
# a, b, c = int(input()), int(input()), int(input())
# print((a+b > c) and (a+c > b) and (b+c > a))

# equation
# a, b, c = int(input()), int(input()), int(input())
# if a == 0:
#     if c != 0:
#         if b != 0:
#             print(-c / b)
#         else:
#             print("nope")
#     elif b != 0:
#         print("nope")
#     else:
#         print(float("inf"))
# else:
#     d = b*b - 4*a*c
#     if d > 0:
#         print(-b/(2*a) + (d**0.5)/(2*a), -b/(2*a) - (d**0.5)/(2*a))
#     elif d == 0:
#         print(-b/(2*a))
#     else:
#         print("nope")

# 256
# x, y, a, b = int(input()), int(input()), int(input()), int(input())
# print((x == a) or (y == b) or (x - a == y - b) or (a - x == y - b))

# 223
# input()
# arr = input().split()
# n = input()
# c = 0
# for num in arr:
#     if num == n:
#         c += 1
# print(c)

# 65
# input()
# arr = input().split()
# c = 0
# for num in arr:
#     if num[0] != "-":
#         c += 1
# print(c)

# 71
# length = int(input())
# arr = input().split()
# num = 1
# for i in range(length - num, length):
#     print(arr[i], end = " ")
# for i in range(0, length-num):
#     print(arr[i], end = " ")

# 72
# input()
# arr = [int(i) for i in input().split()]
# max = arr[0]
# for i in arr:
#     if i > max:
#         max = i
# print(max)

# 1409
# input()
# arr = [int(i) for i in input().split()]
# min1 = float("inf")
# min2 = float("inf")
# for i in arr:
#     if i < min1:
#         min2 = min1
#         min1 = i
#     elif i < min2 and i != min1:
#         min2 = i
#
# print(min1, min2)