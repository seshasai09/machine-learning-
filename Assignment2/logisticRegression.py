
import numpy as np
import math
class LogisticRegression(object):

    def __init__(self,bias,rate,iterations):
        self.weights = []
        self.bias = bias
        self.learningRate = rate
        self.iterations = iterations
        #constants
        self.ONE = 1.0
        self.ZERO = 0.0
        self.HALF = 0.5

     # the model parameters which are the weights are learned in this function
    def train(self,data,labels):
        self.weights=np.zeros(len(data[0]),dtype='f')

        for i in range(0,self.iterations): # number of rounds
            labels = labels[:, np.newaxis] #making row matrix to column matrix
            data = np.column_stack((data, labels)) # appending labels matirx as last column to data matrix
            np.random.shuffle(data) #shuff data
            labels, data = data[:, -1], data[:, :-1] # splitting data into labels and data

            for k in range(0,len(data)):
                val= -(float(self.bias) + np.sum(np.multiply(data[k],self.weights)))
                sigmoidOfVal = 1.0/float(1.0 + math.exp(val))
                error = float(labels[k] - sigmoidOfVal)
                #recomputing weight vector values
                for j in range(0, len(self.weights)):
                    self.weights[j] = float(self.weights[j] + self.learningRate*float(error*data[k][j]))
                self.bias = float(self.bias +self.learningRate*error)




   # To make predictions on test data using the learned model
    def test(self,testData):
        testLabels=[]
        for row in testData:
            val = -(float(self.bias) + np.sum(np.multiply(row,self.weights)))
            estimate = self.ONE / float(self.ONE + math.exp(val))
            if estimate >= self.HALF:
                testLabels.append(self.ONE)
            else:
                testLabels.append(self.ZERO)

        return testLabels









