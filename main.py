import sys


def quicksort_Hoar(data, left=0, right=None):
    pivot = data[left]
    if right is None:
        right = len(data) - 1

    if right <= left:
        return

    i = left
    j = right

    while i <= j:
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1
        if i <= j:
            data[i], data[j] = data[j], data[i]
            movies[i], movies[j] = movies[j], movies[i]
            i += 1
            j -= 1
    quicksort_Hoar(data, left, j)
    quicksort_Hoar(data, i, right)


# print("Num of movies:")
# length = int(input())
# a = dict()
# print("Movies:")
# for k in range(length):
#     a[input()] = k
# movies = list(a.keys())
#
# counter = [0 for _ in range(length)]
# data = sys.stdin.readlines()
# for k in data:
#     if k[:-1] in movies:
#         counter[a[k[:-1]]] += 1
# quicksort_Hoar(counter)
# for k in range(len(counter)):
#     print(movies[len(counter) - k - 1], counter[len(counter) - k - 1])


# example:
# input:
# SW
# SW
# SW
# SW
# LOTR
# SW
# LOTR
# output:
# SW : 5
# LOTR : 2
print("Enter votes:")
a = dict()
data = sys.stdin.readlines()
for k in data:
    if k[:-1] in a:
        a[k[:-1]] += 1
    else:
        a[k[:-1]] = 1
movies = list(a.keys())
values = list(a.values())
quicksort_Hoar(values)
for i in range(len(movies)):
    print(movies[len(movies) - i - 1], ":", values[len(movies) - i - 1])
