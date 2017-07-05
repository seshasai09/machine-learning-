import decisionTree as dt
import numpy as np

def run():
    f = open(r"C:\Seshasai\NEU_MSCS_Course\Spring2017\MachineLearning\materials\ps1\data\badges\badges.training")
    badgesData = []
    for line in f:
        badgesData.append([str(x.strip()) for x in line.split(' ')])
    badgesData = np.array(badgesData)
    label = np.delete(badgesData, np.s_[1:], 1)
    data = np.delete(badgesData, np.s_[0:1], 1)
    temp=[]

    for i in range(0,len(data)):
        temp.append(getFeatuures(data[i]))
    newFeatureData= np.array(temp)
    tree = dt.DecisionTree(newFeatureData, label)
    tree.train()
    f = open(r"C:\Seshasai\NEU_MSCS_Course\Spring2017\MachineLearning\materials\ps1\data\badges\badges.testing")
    badgesData = []
    for line in f:
        badgesData.append([str(x.strip()) for x in line.split(' ')])
    badgesData = np.array(badgesData)
    label = np.delete(badgesData, np.s_[1:], 1)
    data = np.delete(badgesData, np.s_[0:1], 1)
    temp = []

    for i in range(0, len(data)):
        temp.append(getFeatuures(data[i]))
    newFeatureTestData = np.array(temp)
    k = tree.test(newFeatureTestData,2 )
    cnt = 0
    for i in range(0, len(k)):
        if k[i] == label[i]:
            cnt = cnt + 1
            print k[i] + ": ", label[i]
    print float(cnt) / float(len(label))


def getFeatuures(row):
    ans=[]
    ans.append(isFirstCharVowel(row[0]))
    ans.append(isFirstCharVowel(row[1]))
    ans.append(hasCharY(row))
    ans.append(hasCharXorXU(row))
    ans.append(hasCharW(row[0]+row[1]))
    ans.append(hasCharO(row))
    ans.append(hasCharQ(row))
    ans.append(isFirstNameLengtheEqualsSecondName(row))
    ans.append(isLastCharVowel(row[0]))
    ans.append(isLastCharVowel(row[1]))
    return ans

def isFirstCharVowel(str):
    if str[0]=='a' or str[0]=='e' or str[0]=='i' or str[0]=='o' or str[0]=='u':
        return 1
    return 0

def hasCharY(str):
    if 'y' in str[0]:
        return 1
    elif 'y' in str[1]:
        return 1
    return 0


def hasCharXorXU(str):
    name=str[0]+str[1]
    if 'x' in name and 'u' in name:
        return 1
    elif 'x' in name:
        return 1
    return 0
def hasCharW(str):
    if 'w' in str:
        return 1
    return 0

def hasCharO(str):
    if 'o' in str:
        return 1
    return 0
def hasCharQ(str):
    if 'q' in str:
        return 1
    return 0
def isFirstNameLengtheEqualsSecondName(str):
    if len(str[0]) == len(str[1]):
        return 1
    return 0
def isLastCharVowel(str):
    if str[-1]=='a' or str[-1]=='e' or str[-1]=='i' or str[-1]=='o' or str[-1]=='u':
        return 1
    return 0

#run()


