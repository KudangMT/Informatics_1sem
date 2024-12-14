import random


def create_random(size, amp):
    data = []
    for i in range(size):
        data.append(int(random.random() * amp))
    return data

def bin_find(data, num):
    left = 0
    right = len(data) - 1
    while left <= right:
        middle = (left + right)//2
        if data[middle] == num:
            return True
        if num < data[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return False


dat = create_random(50, 100)
dat.sort()
print(dat)
num = int(input())
print(num, "is in data:", bin_find(dat, num))