import math
import heapq
class kNearestNeighbours:

    def __init__(self):
        self.trainData=[]
        self.trainPredict=[]

    def train(self,trainData,trainPredict):
        self.trainData=   trainData
        self.trainPredict= trainPredict
        
    
    def test(self,data,n):
        sol=[]
        for i in range(0,len(data)):
            heap=[]
            for k in range(0,len(self.trainData)):
                dist = self.L2(data[i],self.trainData[k])
                heap.append([dist,self.trainPredict[k]])
            sol.insert(i,self.predict(heap,n))
        return sol


    def L2(self,data,trainData):
        sum=0
        for i in range(0, len(data)):
            if data[i]!=0:
                sum = sum + math.pow(data[i]-trainData[i],2)
        return math.sqrt(sum) 

    def predict(self,heap,n):
        h=heapq.nsmallest(n,heap)
        dict={}
        max=0
        val=""
        for i in range(0,len(h)):
            k,j=h[i]
            if j in dict:
                dict[j]=dict[j]+1
            else:
                dict[j]=1
        #print dict
        for key in dict:
           if max<dict[key]:
               max = dict[key]
               val=key
        return val
                        
                
                
    
    
