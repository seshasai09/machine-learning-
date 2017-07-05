import numpy as np
import math



class Winnow:

    '''
    Constructor for the class winnow
    @params
    weights: a numpy array parameters that are to be learned by winnow
    theta: threshod value in the winnnow equation passed by the user
    mistakes: is a list with cumulative count of mistakes whenever a mistake is made
    instanceWhereMistake:  is a list to keep track of instances where mistakes was made
    actualTrain: boolean variable
    '''

    def __init__(self,weights,theta):
        self.weights = weights
        self.theta = theta
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
    def train(self,data,labels,eta,gamma):
        for i in range(len(data)):
            if (labels[i] * (np.sum(self.weights*data[i]) - self.theta)) <= gamma :
                if self.actualTrain and (labels[i]*(np.sum(self.weights*data[i]) - self.theta))<0:
                    self.storeMistakes(i)
                for j in range(len(self.weights)):
                    self.weights[j] =self. weights[j] * (eta**(labels[i]*data[i][j]))

    '''
    @params:
    testData: a 2D numpy array
    returns: labels for the testData
    '''
    def predict(self, testData):
        labels = []
        for row in testData:
            if np.sum(self.weights * row) - self.theta >=0:
                labels.append(1)
            else:
                labels.append(-1)
        return labels

    '''
    @params:
    noOfAttributes: length of attributes
    '''
    def initializeWeights(self,noOfAttributes):
        self.weights = np.ones(noOfAttributes)

    def storeMistakes(self,instance):

        if(len(self.mistakes)>0):
            k=self.mistakes[len(self.mistakes)-1]
            self.mistakes.append(k+1)
        else:
            self.mistakes.append(1)

        self.instanceWhereMistake.append(instance)

    def getInstanceNMistakes(self):
        return (self.instanceWhereMistake,self.mistakes)

    def setInstanceNMistakes(self):
        self.instanceWhereMistake=[]
        self.mistakes=[]





