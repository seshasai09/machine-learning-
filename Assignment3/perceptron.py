import numpy as np


class Perceptron(object):

    '''
        Constructor for the class Perceptron
        @params
        weights: a numpy array parameters that are to be learned by Perceptron
        bias: threshod value in the Perceptron equation passed by the user
        mistakes: is a list with cumulative count of mistakes whenever a mistake is made
        instanceWhereMistake:  is a list to keep track of instances where mistakes was made
        actualTrain: boolean variable
        '''
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
        self.mistakes = []
        self.instanceWhereMistake = []
        self.actualTrain = False

    '''
    @params:
    data: a 2D numpy array
    labels: a 1D numpy array
    eta: learning rate for winnow algorithm
    gammma: margin for winnow algorithm
    '''
    def train(self, data, labels, eta, gamma):
        for i in range(0, len(data)):
            if (labels[i] * (np.sum(self.weights * data[i]) + self.bias)) <= gamma:
                if self.actualTrain and (labels[i] * (np.sum(self.weights * data[i]) + self.bias)) < 0:
                    self.storeMistakes(i)
                self.weights = self.weights + eta * labels[i] * data[i]
                self.bias = self.bias + eta * labels[i]

    '''
    @params:
    testData: a 2D numpy array
    returns: labels for the testData
    '''
    def predict(self, testData):
        labels = []
        for row in testData:
            if (np.sum(self.weights * row) + self.bias) >= 0:
                labels.append(1)
            else:
                labels.append(-1)
        return labels

    '''
        @params:
        noOfAttributes: length of attributes
        '''
    def initializeWeights(self, noOfAttributes):
        self.weights = np.zeros(noOfAttributes)
        self.bias = 0

    def storeMistakes(self, instance):
        if (len(self.mistakes) > 0):
            k = self.mistakes[len(self.mistakes) - 1]
            self.mistakes.append(k + 1)
        else:
            self.mistakes.append(1)

        self.instanceWhereMistake.append(instance)

    def getInstanceNMistakes(self):
        return (self.instanceWhereMistake, self.mistakes)

    def setInstanceNMistakes(self):
        self.instanceWhereMistake = []
        self.mistakes = []


