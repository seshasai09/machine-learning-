import extra_multi
import extra_binary
import binarydt
import run
import sys
import numpy as np

def main():
    format=sys.argv[1]
    type=sys.argv[2]
    inputFile = sys.argv[3]
    outputFile=sys.argv[4]
    if type=='s':
        if format=='b':
            dataForBDTreeStandard(inputFile,outputFile)
        else:
            dataForMDTreeStandard(inputFile, outputFile)
    else:
        if format=='b':
            dataForBDTExtra(inputFile,outputFile)
        else:
            dataForMDTExtra(inputFile, outputFile)


def dataForMDTExtra(inputFile, outputFile):
    f = open(inputFile)
    badgesData = []
    for line in f:
        badgesData.append([str(x.strip()) for x in line.split(' ')])
    badgesData = np.array(badgesData)
    label = np.delete(badgesData, np.s_[1:], 1)
    data = np.delete(badgesData, np.s_[0:1], 1)
    temp = []

    for i in range(0, len(data)):
        temp.append(getFeaturesMulti(data[i]))
    newFeatureData = np.array(temp)
    writeToFile(newFeatureData,outputFile,label)


def writeToFile(data,outputFile,label):
    outputF = open(outputFile, 'w')
    for i in range(0, len(data)):
        p = ','.join(map(str, data[i]))
        p = p + "," + str(label[i][0])
        outputF.write(p + "\n")
    outputF.close()
    print "writing file to output"


def dataForBDTExtra(inputFile,outputFile):
    f = open(inputFile)
    badgesData = []
    for line in f:
        badgesData.append([str(x.strip()) for x in line.split(' ')])
    badgesData = np.array(badgesData)
    label = np.delete(badgesData, np.s_[1:], 1)
    data = np.delete(badgesData, np.s_[0:1], 1)
    temp = []

    for i in range(0, len(data)):
        temp.append(getFeatures(data[i]))
    newFeatureData = np.array(temp)
    writeToFile(newFeatureData, outputFile, label)


def dataForBDTreeStandard(inputFile,outputFile):
    f = open(inputFile)
    badgesData = []
    for line in f:
        badgesData.append([str(x.strip()) for x in line.split(' ')])
    f.close()
    badgesData = np.array(badgesData)
    label = np.delete(badgesData, np.s_[1:], 1)
    data = np.delete(badgesData, np.s_[0:1], 1)
    dictAlpha = {}
    for i in range(0, 26):
        dictAlpha[chr(i + 97)] = i
    dictAlpha[' '] = 26
    a = np.zeros((len(badgesData), 540))
    # print a

    for i in range(0, len(a)):
        data[i][0]
        data[i][1]
        fill(a, i, data[i][0], data[i][1], dictAlpha)

    writeToFile(a, outputFile, label)
    print "exit"

def dataForMDTreeStandard(inputFile,outputFile):
    f = open(inputFile)
    badgesData = []
    for line in f:
        badgesData.append([str(x.strip()) for x in line.split(' ')])
    badgesData = np.array(badgesData)
    label = np.delete(badgesData, np.s_[1:], 1)
    data = np.delete(badgesData, np.s_[0:1], 1)
    dictAlpha = {}
    for i in range(0, 26):
        dictAlpha[chr(i + 97)] = i
    dictAlpha[' '] = 26
    a = np.zeros((len(data), 20))

    for i in range(0, len(a)):
        fill1(a, i, data[i][0], dictAlpha)
        fill2(a, i, data[i][1], dictAlpha)
    # print a[0]
    writeToFile(a, outputFile, label)


def fill(a,i,str1,str2,dictAlpha):

    if len(str1)>10:
        for z in range(0,10):
            k=dictAlpha[str1[z]]
            a[i][27*z + k]=1
    else:
        for z in range (0, len(str1)):
            k=dictAlpha[str1[z]]
            a[i][27*z + k]=1
        for z in range(len(str1),10):
            a[i][27*z + 26]=1

    if len(str2)>10:
        for z in range(10,20):
            k=dictAlpha[str2[z-10]]
            a[i][27*z + k]=1
    else:
        for z in range (10,len(str2)+10):
            k=dictAlpha[str2[z-10]]
            a[i][27*z + k]=1
        for z in range(10+len(str2),20):
            a[i][27*z + 26]=1

def fill1(a,i,k,dictAlpha):
    if len(k)>10:
        for z in range(0,10):
            a[i][z]=dictAlpha[k[z]]

    else:
        for z in range(0,len(k)):
            a[i][z]=dictAlpha[k[z]]
        for z in range(len(k),10):
            a[i][z]=dictAlpha[' ']

def fill2(a,i,k,dictAlpha):
    if len(k)>10:
        for z in range(10,20):
            a[i][z]=dictAlpha[k[z-10]]

    else:
        for z in range(10,10+len(k)):
            a[i][z]=dictAlpha[k[z-10]]
        for z in range(10+len(k),20):
            a[i][z]=dictAlpha[' ']

def getFeatures(row):
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


def getFeaturesMulti(row):
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










if __name__=='__main__':
    main()