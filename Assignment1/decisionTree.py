import math
import tree
import numpy as np
class DecisionTree:

    def __init__(self,data,predctions):

        self.trainData=data
        self.trainPredict=predctions
        self.entropy=float(0.0)
        self.sol=None
        self.attribuValues=self.getValuesForAttributes(data)
        self.attributes=set([x for x in range(0,len(data[0]))])


    def getValuesForAttributes(self, data):
        dict={}
        for i in range(0,len(data[0])):
            val=set()
            for j in range(0,len(data)):
                if data[j][i] not in val:
                    val.add(data[j][i])
            dict[i]=val
        return dict

    def train(self):
        self.sol=self.id3(self.trainData,self.trainPredict,self.attributes,"")
        #print self.sol

    def print_tree(self,root,h,space):
        if(root!=None and (root.children==None or len(root.children)==0)):
            print space + "label" + " :" + str(root.prediction)
            return

        h=h+1
        print space +"Feature: " +str(root.attribute) +", Information Gain :"+ str(root.informationGain)
        for v in root.children:
            self.print_tree(root.children[v],h,space+" ")

        
    def test(self,testData,n):
        ans=[]
        height=1
        for row in testData:
            model=self.sol
            height=1
            while model!=None and len(model.children)!= 0:
                if(height==n):
                    ans.append(model.prediction)
                    break
                value = row[model.attribute]
                if value in model.children:
                    model = model.children[value]
                    height=height+1
                else:
                    print "no more children"
                    ans.append(model.prediction)
                    break
               # print value
                if len(model.children)==0:
                    ans.append(model.prediction)

                    
        return ans
            

    def id3(self,trainData,predictions,attributes,commonPredict):
        self.entropy=self.getEntropy(predictions)
        root= tree.Tree() 
        if self.entropy==0:
            root.prediction=str(predictions[0][0])
            return root
        elif len(attributes)==0 and len(trainData)>0 and len(predictions):
            root.prediction=self.getMostCommonPredcition(trainData,predictions)
            return root
        elif len(attributes)==0:
            root.prediction=str(commonPredict)
            return root
        else:
            p=self.getBestAttribute(trainData,predictions,attributes)
            k= p[0]
            root.setAttribute(k)
            root.informationGain=p[1]
            values=self.attribuValues[k]
            attributes.discard(k)
            newAttributes = set(attributes)
            for v in values:
                newpredictions = self.getPredictionsForAttribute(k,v,trainData,predictions)
                newtrainData = self.getTrainDataForAttribute(k,v,trainData)
                commonPredict=self.getMostCommonPredcition(trainData,predictions)
                root.prediction=str(commonPredict)
                if len(newtrainData)==0:
                    root.children[v]=tree.Tree()
                    root.children[v].prediction=str(commonPredict)
                else:
                    root.children[v]=self.id3(newtrainData,newpredictions,newAttributes,commonPredict)

        return root
                    
                    
                
            
            
                


#select the best attribute as root of the tree. We do
# this by computing the the information gain

    def getBestAttribute(self,trainData,predictions,attributes):
        entropy = self.getEntropy(predictions)
        maxGain=-1
        ans=None
        sol=[]
        for a in attributes:
            p=self.getPredictionsData(a,trainData,predictions)
            gain=0
            k=0
            for val in p:
                subEntropy=self.getEntropy(p[val])
                k= k + subEntropy*len(p[val])/len(predictions)
                    
            gain = entropy - k
            
            if gain > maxGain :
                ans=a
                maxGain= gain
            if ans==None and entropy==k:
                ans=a
        sol.append(ans)
        sol.append(maxGain)
        return sol
            
        
        
    def getTrainDataForAttribute(self,attribute,value,trainData):
        data=[]
        for row in trainData:
            if row[attribute] == value:
                data.append(row)
        return np.array(data)
        

    def getMostCommonPredcition(self, data,predictions):
        dict={}
        max=0
        pred=None
        for row in predictions:
            if row[0] in dict:
                dict[row[0]] = dict[row[0]] +1
            else:
                dict[row[0]]=1

        for key in dict:
            if dict[key]>max:
                max = dict[key]
                pred=key
        return pred
                
            

    def getPredictionsForAttribute(self,attribute,value,trainData,predictions):
        data=[]
        for i in range(0,len(trainData)):
            if trainData[i][attribute]== value:
                data.append(predictions[i])
        return np.array(data)

# for each attribute and for the values of the attribute
# we get the count of predictions
    def getPredictionsData(self,attribute,trainData,predictions):
        dict={}
        for val in self.attribuValues[attribute]:
            k=[]
            for i in range(0,len(trainData)):
                if trainData[i][attribute]==val:
                    k.append(predictions[i])
            dict[val]=k
        return dict
        

    def getEntropy(self,data):
        dict={}
        for x in data:
            if x[0] in dict :
                dict[x[0]] = dict[x[0]] + 1
            else:
                dict[x[0]] = 1
        k=0
        for key in dict:
            #print float(dict[key])/float(len(data))
            p=float(dict[key])/float(len(data))
            if p != 0:
                k= k - float(p)*float(math.log(p,2))

        return k


    
