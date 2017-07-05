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
    print newFeatureData
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
    k = tree.test(newFeatureTestData,7)
    cnt = 0
    for i in range(0, len(k)):
        if k[i] == label[i]:
            cnt = cnt + 1
            print k[i] + ": ", label[i]
    print float(cnt) / float(len(label))


def getFeatuures(row):
    ans=[]
    l=len(row[0]) + len(row[1])
    ans.append(l)
    ans.append(len(row[0]))
    ans.append(len(row[1]))
    k=numberOfVowels(row[0]+row[1])
    ans.append(k)
    p= l-k
    ans.append(p)
    ans.append(k%2)
    ans.append(p%2)
    ans.append(l%2)
    ans.append(uniqueCharacters(row[0]+row[1]))
    return ans

def numberOfVowels(str):
    cnt=0
    for i in range(0,len(str)):
        if str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u':
            cnt = cnt + 1
    return cnt

def uniqueCharacters(str):
    dict=set()
    for i in range(0,len(str)):
        dict.add(str[i])
    return len(dict)

#run()

if __name__=='__main__':
    run()