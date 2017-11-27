# -*- coding:utf8 -*-

import math


# 加载数据
def loadData(fileName):
    trainSet = []
    with open(fileName) as f:
    # without close
    # f = open(fileName)
        for line in f.readlines():
            line = line.strip().split(',')
            trainSet.append(line)
        featurn = trainSet.pop(0)
    return featurn, trainSet

# 数值化
def numberize():
    pass

# 归一化

# 距离
def distance(vecA, vecB):
    return math.sqrt(sum(((vecA - vecB)**2)))


def kNN(k):
    pass

if __name__ == '__main__':
    featurn, trainSet = loadData('../data/train.csv')
    print(featurn)
