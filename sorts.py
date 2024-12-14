import time
import random
import matplotlib.pyplot as plt


def bubble_sort(data):
    flag = 1
    c = 0
    while flag:
        flag = 0
        c += 1
        for i in range(len(data) - c):
            if data[i] > data[i + 1]:
                data[i + 1], data[i], flag = data[i], data[i + 1], 1
    return data


def selection_sort(data):
    i = 0
    for c in range(0, len(data) - 1):
        maximum = data[0]
        for j in range(0, len(data) - c):
            if data[j] >= maximum:
                maximum = data[j]
                i = j
        data[len(data) - c - 1], data[i] = data[i], data[len(data) - c - 1]
    return data


def insertion_sort(data):
    for i in range(1, len(data)):
        j = i
        while j > 0 and data[j - 1] > data[j]:
            data[j], data[j - 1] = data[j - 1], data[j]
            j -= 1
    return data


def count_sort(data):
    counter = [0 for _ in range(0, 10)]
    res = []
    for k in data:
        counter[k] += 1
    for i in range(0, 10):
        res.append([i for _ in range(counter[i])])
    return res


def merge_sort(data):
    if len(data) == 1:
        return data
    else:
        data1, data2 = merge_sort(data[0:len(data) // 2]), merge_sort(data[len(data) // 2:len(data)])
        i = 0
        j = 0
        s = len(data)
        res = []
        while i + j < s:
            if i == len(data1):
                res.append(data2[j])
                j += 1
            elif j == len(data2):
                res.append(data1[i])
                i += 1
            else:
                if data1[i] > data2[j]:
                    res.append(data2[j])
                    j += 1
                else:
                    res.append(data1[i])
                    i += 1
        return res


def quicksort(data):
    if len(data) < 2:
        return data
    pivot = data[0]
    return quicksort([x for x in data if x < pivot]) + [x for x in data if x == pivot] + quicksort(
        [x for x in data if x > pivot])


def create_random(size, amp):
    data = []
    for i in range(size):
        data.append(int(random.random() * amp))
    return data


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
            i += 1
            j -= 1
    quicksort_Hoar(data, left, j)
    quicksort_Hoar(data, i, right)


def quicksort_quickselect(data):
    return True
def heap_add(A, value):
    A.append(value)
    i = len(A) - 1
    while i > 0 and A[i] > A[(i - 1) // 2]:
        A[i], A[(i - 1) // 2] = A[(i - 1) // 2], A[i]
        i = (i - 1) // 2


def heap_pop(A):
    res = A[0]
    A[0] = A.pop()
    i = 0
    j = 2 * i + 1
    k = 2 * i + 2
    while j < len(A):
        if k < len(A):
            if A[j] >= A[k] and A[j] >= A[i]:
                A[i], A[j] = A[j], A[i]
                i = j
            elif A[k] >= A[j] and A[k] >= A[i]:
                A[i], A[k] = A[k], A[i]
                i = k
            else:
                return res
        else:
            if A[i] < A[j]:
                A[i], A[j] = A[j], A[i]
                i = j
        j = 2 * i + 1
        k = 2 * i + 2
    return res


ran = range(0, 12)
graph = [[0, 0, 0, 0, 0] for i in ran]
for _ in range (0, 10):
    for n in ran:
        tim = time.time()
        bubble_sort(create_random(2 ** n, 1000))
        graph[n][0] += time.time() - tim
        tim = time.time()
        insertion_sort(create_random(2 ** n, 1000))
        graph[n][1] += time.time() - tim
        tim = time.time()
        selection_sort(create_random(2 ** n, 1000))
        graph[n][2] += time.time() - tim
        tim = time.time()
        merge_sort(create_random(2 ** n, 1000))
        graph[n][3] += time.time() - tim
        tim = time.time()
        quicksort(create_random(2 ** n, 1000))
        graph[n][4] += time.time() - tim
plt.plot(graph)
plt.show()

# n = 1000000
# amp = 10000
# print("n =", n)

# inp = create_random(n, amp)
# tim = time.time()
# bubble_sort(inp)
# tim1 = time.time() - tim
# print("bubble:", tim1)
#
# inp = create_random(n, amp)
# tim = time.time()
# a2 = selection_sort(inp)
# tim2 = time.time() - tim
# print("selection:", tim2)
#
# inp = create_random(n, amp)
# tim = time.time()
# a3 = insertion_sort(inp)
# tim3 = time.time() - tim
# print("insertion:", tim3)

# inp = create_random(n, amp)
# tim = time.time()
# a4 = merge_sort(inp)
# tim4 = time.time() - tim
# print("merge:", tim4)

# inp = create_random(n, amp)
# tim = time.time()
# a5 = quicksort(inp)
# tim5 = time.time() - tim
# print("quicksort:", tim5)
#
# inp = create_random(n, amp)
# tim = time.time()
# a5 = quicksort_Hoar(inp)
# tim5 = time.time() - tim
# print("quicksort_hoar:", tim5)

# inp = create_random(n, 10)
# tim = time.time()
# a6 = count_sort(inp)
# tim6 = time.time() - tim
# print("count_sort:", tim6)

# inp = create_random(n, 10)
# tim = time.time()
# inp.sort()
# tim7 = time.time() - tim
# print("python_sort:", tim7)
