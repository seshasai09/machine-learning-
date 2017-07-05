import numpy as np
import winnow
import readData as rd

TEN_PERCENT=10.0/100.0
TWENTY_PERCENT=20.0/100.0
PERCENT_OF_DATA=100/100

#this function takes in filename to read data from
# splits the data to D1, D2 and D3
# return the number of mistakes made with margin and without margin
def driver(trainfileName,testFileName,n):
    print trainfileName

    tempData,tempLabels = rd.readDataFromFile(trainfileName,PERCENT_OF_DATA)
    labels = np.array(tempLabels)
    data = rd.createNumpyArrayOfData(tempData,n)


    d1= data[0:TEN_PERCENT*len(data)]
    l1=labels[0:TEN_PERCENT*len(data)]
    d2 = data[TEN_PERCENT*len(data):TWENTY_PERCENT*len(data)]
    l2 = labels[TEN_PERCENT*len(data):TWENTY_PERCENT*len(data)]
    d3 = data[TWENTY_PERCENT*len(data):]
    l3 = labels[TWENTY_PERCENT*len(data):]


    model = winnow.Winnow(None, n+1)

    ######## train the model without margin and with learning rate
    gammaNeta=withoutMargin(d1,l1,d2,l2,model)
    print gammaNeta

    rd.trainModel(d3,l3,model,gammaNeta)
    if testFileName !=None:
        tempTestData,tempTestLabels = rd.readDataFromFile(testFileName,100)
        rd.getAccuracy(tempTestLabels,tempTestData,model,n)


    winnowWithoutMargin=model.getInstanceNMistakes()

    model.actualTrain = False
    ######## train the model with margin and with learning rate and identify the best learning rate and margin
    gammaNeta = withMargin(d1,l1,d2,l2,model)
    print gammaNeta

    rd.trainModel(d3,l3,model,gammaNeta)
    if testFileName !=None:
        tempTestData,tempTestLabels = rd.readDataFromFile(testFileName,100)
        rd.getAccuracy(tempTestLabels,tempTestData,model,n)
    winnowWithMargin = model.getInstanceNMistakes()

    return winnowWithoutMargin,winnowWithMargin


# function to identify the best learning rate for the given data
def withoutMargin(d1,l1,d2,l2,model):
    model.initializeWeights(len(d1[0]))
    gamma = 0
    eta=[1.1,1.01,1.005,1.0005,1.0001]
    accuracy = 0.0
    for j in eta:
        tempAccuracy = callWinnow(d1, l1, d2, l2, j, gamma, model)

        if tempAccuracy > accuracy:
            gammaNeta = (gamma, j)
            accuracy = tempAccuracy
    print  accuracy
    return gammaNeta


# function to identify the best learning parameters for the given data
def withMargin(d1,l1,d2,l2,model):
    gamma=[2.0,0.3,.04,.006,.001]
    eta = [1.1, 1.01, 1.005, 1.0005, 1.0001]
    accuracy=0.0
    weights = np.ones(len(d1[0]))
    model.weights = weights
    for i in gamma:
        for j in eta:
            tempAccuracy = callWinnow(d1,l1,d2,l2,j,i,model)

            if tempAccuracy > accuracy:
                gammaNeta=(i,j)
                accuracy = tempAccuracy
    print accuracy
    return gammaNeta


def callWinnow(d1,l1,d2,l2,eta,gamma,model):
    model.initializeWeights(len(d1[0]))
    for i in range(0,20):
        model.train(d1,l1,eta,gamma)
    l2_predict =model.predict(d2)
    cnt=0
    for i in range(0,len(l2_predict)):
        if l2_predict[i] == l2[i]:
            cnt = cnt +1

    return 100.0*cnt/len(l2)



# def readDataFromFile(fileName,percentOfData):
#     f = open(fileName)
#     tempLabels=[]
#     tempData=[]
#     for line in f:
#         line= line.strip("\n").split(" ")
#         if((line[0])== "+1"):
#             tempLabels.append(1)
#         else:
#             tempLabels.append(-1)
#         tempData.append(line[1:])
#     return tempData[0:percentOfData*(len(tempData))],tempLabels[0:percentOfData*len(tempLabels)]

# def createNumpyArrayOfData(tempData,n):
#     data = np.zeros((len(tempData), n + 1))
#     for i in range(0, len(tempData)):
#         for j in range(0,len(tempData[i])):
#            # print tempData[j][j]
#             k=str(tempData[i][j]).split(":")
#             data[i][int(k[0])]=1
#     return data








#driver()
