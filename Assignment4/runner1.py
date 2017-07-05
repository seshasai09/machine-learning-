import numpy as np
import interface2
def start():


    tempData = readData(r"data/mnist_train.csv") #loading train data
    tempTestData = readData(r"data/mnist_test.csv") #loading test data


   #creating numpy array representation of data
    npTempData = np.array(tempData,dtype='float32')
    npTestData = np.array(tempTestData, dtype='float32')
    np.random.shuffle(npTempData)


    labels = npTempData[:,0:1]
    data = npTempData[:,1:]
    #20% validation dataset
    validationData = data[0:.20*len(data)]
    validationLabels = labels[0:.20 * len(labels)]
    validationLabels = numpyLabels(validationLabels)
    # 80% train data set
    trainData = data[.20 * len(data):]
    trainLabels = labels[.20 * len(labels):]
    trainLabels = numpyLabels(trainLabels)
    # testdata
    testLabels = npTestData[:, 0:1]
    testData = npTestData[:, 1:]

    # initializing neural netwrok class
    network1 = interface2.Network(len(trainData[0]), 300, 10, .000004)
    #training the network
    network1.trainNetwork(trainData, trainLabels, validationData, validationLabels)
    predictedLabels = network1.testNetwork(testData)
    accuracy(predictedLabels,testLabels)


def accuracy(predictedLabels,validationLabels):
    cnt =0
    for i in range(len(predictedLabels)):
        if np.argmax(predictedLabels[i]) == validationLabels[i]:
            cnt = cnt + 1

    print float(cnt)/float(len(validationLabels))


def numpyLabels(trainLabels):
    labels = np.zeros((len(trainLabels),10))
    for i in range(len(trainLabels)):
        labels[i][trainLabels[i][0]]=1
    return labels

def readData(filename):
    f = open(filename)
    data=[]
    for line in f:
        line = line.strip().split(",")
        line.append('1')
        data.append(line)
    return data







start()

