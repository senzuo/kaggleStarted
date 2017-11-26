# -*- coding:utf8 -*-

# 加载数据
def loadData(fileName):
    trainSet = []
    # with open(fileName) as f:
    f = open(fileName)
    for line in f.readlines():
        line = line.strip().split(',')
        trainSet.append(line)
    featurn = trainSet.pop(0)
    return featurn, trainSet

# 距离
def distance(vecA, VecB):


def kNN(k)

if __name__ == '__main__':
    featurn, trainSet = loadData('../data/train.csv')
    print(trainSet)
