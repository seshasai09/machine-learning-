
import neuron as n
import numpy as np
class Network(object):


    #constuctor of the class
    """
    @args:
    featureLength: count of node in input layer
    noOfNeuronsL1: count of nodes in hidden layer
    noOfNeuronsL2: count of nodes in output layer
    eta
    """
    def __init__(self, featureLength, noOfNeuronsL1, noOfNeuronsL2, eta):
        self.weights1=np.random.normal(0.0,pow(featureLength,-.005),(featureLength,noOfNeuronsL1))
        self.weights2 = np.random.normal(0.0, pow(noOfNeuronsL1+1, -.005), (noOfNeuronsL1+1, noOfNeuronsL2))
        self.eta= eta

    '''
    @args
    trainData: training data in numpy format
    trainLabels: train data labels in numpy format
    validationData: validation data in numpy formt
    validationLabels: in numpy format
    '''
    def trainNetwork(self,trainData,trainLabels,validationData,validationLabels):
        self.bias = np.random.rand(len(trainData), 1)
        lis1 = []
        lis2 = []

        for i in range(0,100):
            z1= n.neuron(self.weights1,trainData,"tanh")
            z1 = np.column_stack((z1,self.bias))
            z2 = n.neuron(self.weights2,z1,"sigmoid")
            ###### batch gradient descent
            diff = (z2-trainLabels)
            delta2 = np.dot(z1.transpose(),diff)  # gradient of loss function w.r.t to ouput layer weights
            self.weights2 = self.weights2 - self.eta*delta2 #output layer weight updates
            temp1 =np.dot(diff,self.weights2.transpose())
            temp2 = np.multiply(temp1,(1-np.multiply(z1,z1)))
            delta1 = np.dot(trainData.transpose(),temp2)  #gradient of loss function w.r.t to hidden layer weights
            self.weights1 = self.weights1 - self.eta*delta1[:,0:300] # hidden layer weight update
            labels = self.testNetwork(validationData)
            labelsTrain = self.testNetwork(trainData)
            k = self.accuracy(labels, validationLabels)
            p = self.accuracy(labelsTrain, trainLabels)
            lis1.append(k)
            lis2.append(p)
        self.writetofile(lis1, lis2)




   #function to test the model
    def testNetwork(self,testData):
        z1 = n.neuron(self.weights1, testData, "tanh")
        bias = np.ones((len(z1), 1))

        z1 = np.column_stack((z1, bias))
        z2 = n.neuron(self.weights2, z1, "sigmoid")
        return z2

    def accuracy(self, predictedLabels, validationLabels):
        cnt = 0
        for i in range(len(predictedLabels)):
            if np.argmax(predictedLabels[i]) == np.argmax(validationLabels[i]):
                cnt = cnt + 1

        return float(cnt) / float(len(validationLabels))

    def writetofile(self, val, train):
        f = open("sol.txt", 'w')
        for i in range(len(val)):
            f.write(str(val[i]) + "," + str(train[i]))
        f.close()




