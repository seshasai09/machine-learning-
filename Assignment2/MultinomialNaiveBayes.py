import math
import sys
class NaiveBayes(object):

    def __init__(self,classes,classData,data):
        self.classes = classes  # prior data for all the classes
        self.priors={} # saves prior probability for each class
        self.classData = classData # hasmap with key as class and value as file name for data for the class
        self.data = data
        self.probabilities = {}

    def train(self):
        classes = self.getUniqueClassesInData()
        #print classes
        for item in classes:
            self.priors[item]=self.getPriorValue(item)
            dataForItem = self.getDataForItem(item)
            countOfInItem = self.getCountOfInItem(dataForItem)
            wProbabilitiiesForItem={}
            for w in self.data:
                if w in dataForItem.keys():
                    countOfWInItem = float(dataForItem[w])
                else:
                    countOfWInItem = 0.0
                probabilityOfWInItem = float((countOfWInItem + 1.0))/float((countOfInItem + len(self.data)))
                wProbabilitiiesForItem[w]=probabilityOfWInItem


            self.probabilities[item] = wProbabilitiiesForItem



    def test(self,testData):
        sol = []

        for row in testData:
            max = 1 - sys.maxint
            temp=None
            for c in self.probabilities.keys():
                val=1.0
                mapOfClass = self.probabilities[c]
                for w in row:
                    val =float(val) +  math.log(float(mapOfClass[w]))

                val=  val + math.log( self.priors[c])
                if val > max:
                    temp=c
                    max=val

            sol.append(temp) # class is max of sol[c]

        return sol


    def getCountOfInItem(self,dataForItem):
        cnt=0
        for key in dataForItem.keys():
            cnt = cnt + dataForItem[key]
        return cnt


    def getDataForItem(self,item):

        dict={}
        f= open(self.classData[item])
        for line in f.readlines():
           k= line.split(" ")
          # print k[0]
           dict[k[0]]=int(k[1].strip("\n"))
        return dict



    def getPriorValue(self,item):
        cnt =0.0
        for i in self.classes:
            if i==item:
                cnt = cnt + 1
        return float(cnt/len(self.classes))

    def getUniqueClassesInData(self):
        classes = set()
        for c in self.classes:
            classes.add(c)
        return classes


    def printPriorVallues(self):
        for row in self.priors:
            print self.priors[row]