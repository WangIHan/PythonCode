import matplotlib.pyplot as plt
import pandas as pd
import re
import sys
from mpl_toolkits.mplot3d import Axes3D
import numpy
import random
"""src = r'./dataSet.txt'
file = open(src)
line = file.readlines()
while line:

data = pd.read_table(r"./dataSet.txt")
print(data)"""
data = [
    [31,65,4,1],
    [33,58,10,1],
    [33,60,0,1],
    [34,59,0,2],
    [34,66,9,2],
    ]
data1 = data[data[3] == 1]  # status为1的数据
data2 = data[data[3] == 2]  # status为2的数据


def showDataModule(data1, data2):
    fig = plt.figure(figsize=(16, 12))
    ax = fig.gca(projection="3d") #get current axis
    ax.scatter(data1[1], data1[2], data1[3], c='r', s=100, marker="*", label="survived 5 years or longer") #status为1的样本的散点图
    ax.scatter(data2[1], data2[2], data2[3], c='b', s=100, marker="^", label="died within 5 year") #status为2的样本的散点图
    ax.set_xlabel("", size=15)
    ax.set_ylabel("", size=15)
    ax.set_zlabel("", size=15)
    ax.set_title('', size=15, weight='bold')
    ax.set_zlim(0, 30)
    ax.legend(loc="lower right", fontsize=15)
    plt.show()


# showDataModule(data1, data2)
"""list1 = numpy.linspace(0.0, 100.0, 150)
print(list1)
numpy.
for i in range(150):
    index
list1 = random.sample(list1, 150)"""
# 自动生成成绩
list_f = []
list1 = range(300, 1000)
# 相似度
list_a = random.sample(list1, 150)
list_a.sort()
# 贴切度
list2 = range(400, 1000)
list_b = random.sample(list2, 150)


list3 = range(400, 1000)
list_c = random.sample(list3, 150)

list4 = range(600, 1000)
list_d = random.sample(list4, 150)

list_i = []
for index in range(150):
    list_t = []
    list_t.clear()
    list_t.append(list_a[index]/10.0)
    list_t.append(list_b[index]/10.0)
    list_t.append(list_c[index]/10.0)
    list_t.append(list_d[index]/10.0)
    list_f.append(list_t)
"print((list_f))"


def loadDatadet(infile, k):
    f = open(infile,'r')
    sourceInLine = f.readlines()
    dataset = []
    for line in sourceInLine:
        temp1 = line.strip('\n')
        temp2 = re.findall(r'\d+.\d+|\d+', temp1)
        # 1. _123.123_  2. _123.123<br> 标签用2和1中数据量冲突
        dataset.append(temp2)
    for i in range(0, len(dataset)):
        for j in range(k):
            dataset[i].append(float(dataset[i][j]))
        del(dataset[i][0:k])
    return dataset


infile='./dataSet.txt'
k = 5
'''infile = numpy.array(loadDatadet(infile, k))
print('dataset=', infile)

    for j in range(150):
    for k in range(4):
        print(str(list_i[j][k]) + ' ', end="")

    print()'''
