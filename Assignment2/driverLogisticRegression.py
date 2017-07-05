import numpy as np
import logisticRegression as lr
def run():
    model = lr.LogisticRegression(0,.015625,20)
    trainDataLabels=[] # labels for train data set
    testDataLabels = []  # labels for test data set
    rawData = readDataFromFile(r"data\train.libsvm")
    d = open(r"data\features.lexicon")
    lexicon = [line.strip("\n").split(" ")[1] for line in d.readlines()]
    d.close()

    #creating a matrix with rows size equals length of data and columns size equals size of lexicon
    # partial data has value 1 in columns where the attribute is present for the data point
    partialData = np.zeros((len(rawData),len(lexicon)))
    #dict is used  as a placeholder for mapping between word in lexicon and column number
    dict={}
    for i in range(0,len(lexicon)):
        dict[int(lexicon[i])]=i

    for l in range(0,len(rawData)):
        trainDataLabels.append(float(rawData[l][0]))
        k=rawData[l][1:]
        for j in range(0,len(k)):
            p=k[j].split(":")
            partialData[l,dict[int(p[0])]]=1.0


    getLabels(trainDataLabels)
    trainDataLabels = np.array(trainDataLabels)

    # training the model
    model.train(partialData,trainDataLabels)

    # testing the model
    rawData = readDataFromFile(r"data\test.libsvm")
    # partial test data has value 1 in columns where the attribute is present
    partialTestData = np.zeros((len(rawData), len(lexicon)))
    #dict = {}

    for l in range(0, len(rawData)):
        testDataLabels.append(float(rawData[l][0]))
        k = rawData[l][1:]
        for j in range(0, len(k)):
            p = k[j].split(":")
            partialTestData[l, dict[int(p[0])]] = 1.0

    getLabels(testDataLabels)
    testDataLabels = np.array(testDataLabels)

    ans =model.test(partialTestData)
    printSolToFile(ans)


def getLabels(trainDataLabels):
    for i in range(0,len(trainDataLabels)):
        if trainDataLabels[i]==2.0:
            trainDataLabels[i]=1.0
        else:
            trainDataLabels[i] = 0.0

def printSolToFile(ans):
    solFile=open(r"output\predictions.lr",'w')
    for i in range(0,len(ans)):
        if ans[i]== 1.0:
            solFile.write( TWO + NEWLINE)
        else:
            solFile.write(SIX + NEWLINE)


def readDataFromFile(fileLocation):
    f = open(fileLocation)
    data = [line.strip("\n").split(" ") for line in f.readlines()]
    f.close()
    return data




TWO = "2.0"
SIX = "6.0"
NEWLINE="\n"

if __name__ == "__main__":
    run()