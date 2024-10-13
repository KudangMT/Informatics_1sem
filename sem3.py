import time

# 1 --------------------------------
# def fibonacci(n1, n2, c):
#     if c == 1:
#         print(n1 + n2)
#     else:
#         fibonacci(n2, n1 + n2, c - 1)
#
#
# def fib2(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return fib2(n - 1) + fib2(n - 2)
#
#
# def fib3(n, cache):
#     if n == 0 or n == 1:
#         cache[n] = 1
#         return 1
#     if cache[n] != 0:
#         return cache[n]
#     cache[n] = fib3(n - 1, cache) + fib3(n - 2, cache)
#     return cache[n]
#
#
# start = time.time()
# n = 35
#
# fibonacci(0, 1, n)
# print("dt: ", time.time() - start)
# start = time.time()
#
# print(fib2(n))
# print("dt: ", time.time() - start)
# start = time.time()
#
# cache = [0 for i in range(n+2)]
# print(fib3(n, cache))
# print("dt: ", time.time() - start)
# start = time.time()


# 2 ---------------------------
# def prime(n):
#     nm = n // 2
#     num = 2
#     while n != 1:
#         if n % num == 0:
#             print(num, end=" ")
#             n /= num
#         else:
#             num += 1
#
# prime(832)

# 3 ---------------------------
# def gcd(a, c):
#     b = min(a, c)
#     a = max(a, c)
#     if a % b == 0:
#         return b
#     else:
#         return gcd(b, a-b)
#
# a = 1
# b = 1
# d = gcd(a, b)
# print(d)

# 5 -------------------------------
def spiral_matrix(nc, mc, nd, md, dir, c):
    n_count = nd
    m_count = md
    while n_count and m_count:
        if dir == 1:
            mat[nc][mc] = c
            c += 1
            nc += 1
            n_count -= 1
        elif dir == 2:
            mat[nc][mc] = c
            c += 1
            mc += 1
            m_count -= 1
        elif dir == 3:
            mat[nc][mc] = c
            c += 1
            nc -= 1
            n_count -= 1
        elif dir == 4:
            mat[nc][mc] = c
            c += 1
            mc -= 1
            m_count -= 1

    if dir == 1 or dir == 3:
        md -= 1
        if c < n+m:
            md += 1
    elif dir == 2 or dir == 4:
        nd -= 1
        if c < n+m:
            nd += 1

    dir += 1
    if dir == 5:
        dir = 1
    if nd == 0 or md == 0:
        return 0
    spiral_matrix(nc, mc, nd, md, dir, c)


n = 9
m = 10
mat = []
for l in range(n):
    mat.append([0 for i in range(m+1)])

spiral_matrix(0, 0, n-1, m-1, 1, 1)
for l in range(m):
    for i in range(n):
        print(mat[i][l], end=" ")
        if mat[i][l] < 10: print(end=" ")
    print()


# 6 -----------------------
# x = [i for i in range(10)]
# y = [6*i for i in range(10)]
# xy = [x[i]*y[i] for i in range(10)]
# xx = [x[i]*x[i] for i in range(10)]
# k = (sum(xy)*len(xx))/(len(xy)*sum(xx))
# print(k)
