import math
import sys
import time

# 1 -------------------------------------------
# def find_k(data, k):
#     arr = data
#     while len(arr) > k:
#         data = arr
#         pivot = data[len(data)//2]
#         arr = [x for x in data if x < pivot]
#     return data
#
# def quicksort(data):
#     if len(data) < 2:
#         return data
#     pivot = data[0]
#     return quicksort([x for x in data if x < pivot]) + [x for x in data if x == pivot] + quicksort(
#         [x for x in data if x > pivot])
#
#
# inp = input().split()
# length = int(inp[0])
# k = int(inp[1])
# data = [int(d) for d in input().split()]
# data = find_k(data, k)
# data = quicksort(data)
# for i in range(k):
#     print(data[i], end = " ")

# 2 ---------------------------------------------------
# def min_cas():
#     m = 0
#     for k in range(len(cas)):
#         if cas[k] < cas[m]:
#             m = k
#     return m
#
# inp = input().split()
# n = int(inp[0])
# k = int(inp[1])
# cas = [0 for _ in range(k)]
#
# data = list(map(int, input().split()))
# for k in data:
#     cas[min_cas()] += k
# print(max(cas))


# 3 -----------------------------------------------------------------
# def tree_add(num, n, k):
#     if tree[k] == 0:
#         tree[k] = num
#         return
#     elif 2*k + 2 <= n:
#         if tree[k] > num:
#             k = 2*k + 1
#         else:
#             k = 2*k + 2
#     else:
#         k = (k-1)//2
#     tree_add(num, n, k)

# def tree_add(num, k):
#     if tree[k] == 0:
#         tree[k] = num
#     else:
#         while True:
#             if num < tree[k]:
#                 if tree[2*k + 1] == 0:
#                     tree[2*k + 1] = num
#                     return
#                 k = 2 * k + 1
#             else:
#                 if tree[3 * k + 2] == 0:
#                     tree[3 * k + 2] = num
#                     return
#                 k = 3 * k + 2
#
#
# n = int(input())
# data = [int(x) for x in input().split()]
# tup = {x for x in data}
# # n = 2 ** math.ceil(math.log2(len(data)))
# # km = int(math.log2(n))
# tree = [0 for _ in range(2 ** n)]
# for num in data:
#     if num in tup:
#         tree_add(num, 0)
#         tup.remove(num)
# print(tree)
# print(len(tree))
# for i in range(0, n):
#     print(tree[(2 ** i)-1: 2 ** (i+1)-1])




# class Node:
#     def __init__(self, value, parent=None, left=None, right=None):
#         self.v = value
#         self.l = left
#         self.r = right
#
# class BinTree:
#     def __init__(self):
#         self.root = None
#
#     def add(self, value):
#         if self.root is None:
#             self.root = Node(value)
#         else:
#             cnode = self.root
#             while True:
#                 if value < cnode.v:
#                     if cnode.l is None:
#                         cnode.l = Node(value, cnode)
#                         return
#                     cnode = cnode.l
#                 else:
#                     if cnode.r is None:
#                         cnode.r = Node(value, cnode)
#                         return
#                     cnode = cnode.r
#
#     def get(self, cnode=0):
#         if cnode == 0:
#             cnode = self.root
#         if cnode is None:
#             return []
#         if cnode.l is None and cnode.r is None:
#             return[cnode.v]
#         else:
#             return (self.get(cnode.l) +
#                 self.get(cnode.r))
#
#
# n = int(input())
# data = [int(x) for x in input().split()]
# tup = {x for x in data}
# tree = BinTree()
# for num in data:
#     if num in tup:
#         tree.add(num)
#         tup.remove(num)
# data = tree.get()
# print(*data)


# 4 -----------------------------------------------------------------
# out = ""
# t = int(input())
# for _ in range(t):
#     inp = input().split()
#     n = int(inp[0])
#     q = int(inp[1])
#     data = list(map(int, input().split()))
#     D = dict()
#     for i in range(n):
#         if data[i] in D:
#             D[data[i]] += 1
#         else:
#             D[data[i]] = 1
#
#     for _ in range(q):
#         inp = input().split()
#         i = int(inp[0])
#         j = int(inp[1])
#         m = 0
#         for k in range(data[i - 1] + 1, data[j - 1]):
#             if k in D:
#                 if m < D[k]:
#                     m = D[k]
#         s = data[i - 1]
#         c = 0
#         l = i
#         while l <= j and data[l - 1] == s:
#             c += 1
#             l += 1
#         if m < c:
#             m = c
#         s = data[j - 1]
#         c = 0
#         while j >= i and data[j - 1] == s:
#             c += 1
#             j -= 1
#         if m < c:
#             m = c
#         out += str(m)+"\n"
# print(out)
# print(time.time() - tim)
# print()
# print(*[str(x) + " "*(3 - len(str(x))) for x in data])
# print(*[str(x) + " "*(3 - len(str(x))) for x in range(1, len(data) + 1)])

class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.v = value
        self.l = left
        self.r = right

class SegTree:
    def __init__(self):
        self.root = 0
        self.k = 0

    def create(self, lis, cnode=None, n=0):
        if not n:
            n = math.ceil(math.log2(len(lis)))
        if cnode is None:
            cnode = self.root
        if n != 1:
            self.create()

    def get(self, cnode=0):
        if cnode == 0:
            cnode = self.root
        if cnode is None:
            return []
        if cnode.l is None and cnode.r is None:
            return[cnode.v]
        else:
            return (self.get(cnode.l) +
                self.get(cnode.r))


n = int(input())
data = [int(x) for x in input().split()]
tree = SegTree()
tree.create(data)
data = tree.get()
print(*data)
