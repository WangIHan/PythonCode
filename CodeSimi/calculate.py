import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt



# 欧式距离
def distance(vector1, vector2):
    d = 0
    for a, b in zip(vector1, vector2):
        d += (a - b) ** 2
    return d ** 0.5

# 余弦相似度
def cos(vector1, vector2):
    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for a, b in zip(vector1, vector2):
        dot_product += a * b
        normA += a ** 2
        normB += b ** 2
    if normA == 0.0 or normB == 0.0:
        return None
    else:
        return dot_product / ((normA * normB)**0.5)

"""
target 0 60 70 80 90 
       0  1  2  3  4    stats_length = 5
"""

"""
train_data：所要划分的样本特征集 
train_target：所要划分的样本结果 
test_size：样本占比，如果是整数的话就是样本的数量 
random_state：是随机数的种子
"""


def kNN(dataSet):
    score_X = []
    score_y = []
# 将原始数据集中的向量部分 和 标签部分拆分出来
    for index in range(len(dataSet)):
        score_y.append(int(dataSet[index].pop(4)))
        score_X.append(dataSet[index])
# 方法一：拆分测试集和训练集,并进行预测
    score_train_X , score_test_X, score_train_y ,score_test_y = train_test_split(score_X, score_y, test_size=0.2,random_state=0)
    # 方法二：拆分测试集和训练集
    np.random.seed(0)
# permutation随机生成0-150的系列
# 新版的numpy需要这样去使用shuffle，train_y是列表，列表元素是array,但是这样无法使用直接获取index.
    indices = np.random.permutation(len(score_y))
    score_X_train = np.array(score_X)[indices[:-30]]
    score_y_train = np.array(score_y)[indices[:-30]]
    score_X_test = np.array(score_X)[indices[-30:]]
    score_y_test = np.array(score_y)[indices[-30:]]
    print(score_X_test)
    """print(score_train_X)
    print(score_train_y)"""
# n_neighbors 取临近点个数
    knn = KNeighborsClassifier(n_neighbors=2)
    knn.fit(score_X_train, score_y_train)
# 结果为 30 x 1 的矩阵 故需对结果进行调整 否则无法直接赋值

    finalSet = knn.predict(score_X_test)

    print('预测结果', finalSet)
    # 计算预测的准确率
    print('预测准确率', knn.score(score_X_test, score_y_test))

    return finalSet