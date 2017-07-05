import numpy as np

#read data from the file and converts it to python list and returns a list

def readDataFromFile(fileName,percentOfData):
    f = open(fileName)
    tempLabels=[]
    tempData=[]
    for line in f:
        line= line.strip("\n").split(" ")
        if((line[0])== "+1"):
            tempLabels.append(1)
        else:
            tempLabels.append(-1)
        tempData.append(line[1:])
    return tempData[0:percentOfData*(len(tempData))],tempLabels[0:percentOfData*len(tempLabels)]


#this function accepts a list and return numpy array representation of the list
def createNumpyArrayOfData(tempData,n):
    data = np.zeros((len(tempData), n + 1))
    for i in range(0, len(tempData)):
        for j in range(0,len(tempData[i])):
           # print tempData[j][j]
            k=str(tempData[i][j]).split(":")
            data[i][int(k[0])]=1
    return data


#this function calls the train method on the model
def trainModel(d3,l3,model,gammaNeta):
    model.actualTrain = True
    model.initializeWeights(len(d3[0]))
    model.setInstanceNMistakes()
    model.train(d3, l3, gammaNeta[1], gammaNeta[0])

#this function calls the predict method on the model and estimates the accuracy
def getAccuracy(tempTestLabels,tempTestData,model,n):
    testLabels = np.array(tempTestLabels)
    testData = createNumpyArrayOfData(tempTestData, n)
    testPredictions = model.predict(testData)
    cnt = 0
    for i in range(0, len(testPredictions)):
        if testPredictions[i] == testLabels[i]:
            cnt = cnt + 1

    print 100.0 * cnt / len(testLabels)


