class Tree(object):

        

    def __init__(self):
        self.attribute=""
        self.children={}
        self.prediction=""
        self.informationGain=0

    def setPrediction(self,label):
        self.prediction=label

    def getPrediction(self):
        return self.prediction

    def setAttribute(self,attr):
        self.attribute=attr

    def getAttribute(self):
        return self.attribute
    
    
