import matplotlib.pyplot as plt
import numpy as np
import math
import random
import pandas as pd

x = [i for i in range(10)]
y = [6 * i for i in range(10)]
xy = [x[i] * y[i] for i in range(10)]
xx = [x[i] * x[i] for i in range(10)]
k = (sum(xy) * len(xx)) / (len(xy) * sum(xx))

# just graph ---------------------------------------
# plt.plot(x, xx)
# plt.plot(x, xy)
# plt.title('Graph')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.xticks([1,3,5,7])
# plt.yticks([0, 100, 200, 300, 400, 500])
# plt.grid()
# plt.show()


# bar diagram
# plt.bar(x, xy)
# plt.bar(x, y)
# plt.title('Graph')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.xticks([1,3,5,7])
# plt.yticks([0, 100, 200, 300, 400, 500])
# plt.grid()
# plt.show()


# histogram
# new_data = list("asdadasmdakscklnkashkkhkkjjkcnkknlsacnklkcass")
# plt.hist(new_data, bins=30)
# plt.title('Histogram')
# plt.xlabel('Letter')
# plt.ylabel('Letters in text')
# plt.show()


# pie diagram
# plt.pie([0.5, 0.31, 0.19], labels = ['No', 'No, but orange', 'No, but green'], rotatelabels = True)
# plt.title('What are the chances that I will wake up early tomorrow?')
# plt.show()


# mix
# data = []
# xhist = [1, 2, 3, 4, 5]
# yhist = [xhist[i]*np.exp(i+1) for i in range(5)]
# for i in range(2000):
#     if i % 2 == 0:
#         data.append(3)
#     if i % 4 == 0:
#         data.append(2)
#     if i % 5 == 0:
#         data.append(1)
#     if i % 8 == 0:
#         data.append(4)
#     if i % 7 == 0:
#         data.append(5)
# plt.hist(data, bins = 5)
# plt.plot(xhist, yhist)
# plt.show()


# normal -------------------------------------------
# nums = np.random.normal(10, 3, 40000) # mean, sigma, size
# plt.hist(nums, 100)
# mean = np.mean(nums)
# print(mean)
# x = [i for i in range(0, 20)]
# y = [((mean ** i)*np.exp(-mean)/math.factorial(i))*10000 for i in range(0, 20)]
# plt.plot(x, y)
# plt.show()


# graph with error -------------------------------
# x = [i + random.random() for i in range(1, 10)]
# y = [i * np.exp(-i + random.random()) for i in range(1, 10)]
# yist = [i * np.exp(-i) for i in range(1, 10)]
# err = (sum([(y[i - 1] - yist[i - 1]) ** 2 for i in range(10)]) / 10) ** 0.5
# print(err)
# plt.scatter(x, y, marker='x')
# plt.errorbar(x, y, yerr=err, xerr=0.5, color='k', linestyle='None', elinewidth=0.5)
# plt.plot(x, y, 'b')
# plt.plot(x, yist, 'r')
# plt.show()


# iris without pandas --------------------------
# file = open("iris_data.csv", "r")
# file.readline()
# data = file.readlines()
# x = []
# y1 = []
# y2 = []
# for line in data:
#     l = line.split(",")
#     x.append(l[0])
#     y1.append(float(l[1]))
#     y2.append(float(l[2]))
# plt.xticks([0, 40, 80, 120])
# plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8])
# plt.plot(x, y1, 'b')
# plt.plot(x, y2, 'k')
# plt.grid()
# plt.show()


# plot with pandas
# df = pd.read_csv('iris_data.csv')
# id = list(df["Id"])
# sl = list(df["SepalLengthCm"])
# sw = list(df["SepalWidthCm"])
# pl = list(df["PetalLengthCm"])
# pw = list(df["PetalWidthCm"])
# plt.plot(sw, sl, 'k')
# plt.plot(sw, pl, 'b')
# plt.plot(sw, pw, 'g')
# plt.plot(sl, pl, 'r')
# plt.plot(sl, pw, 'm')
# plt.plot(pw, pl, 'c')
# plt.show()