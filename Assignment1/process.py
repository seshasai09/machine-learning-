import knn
class Process:

    def __init__(self,trainDataPath,testDataPath):
        self.trainPath=trainDataPath
        self.testPath=testDataPath
        self.trainData=[]
        self.trainDataPredict=[]
        self.testData=[]
        self.testDataPredict=[]
        
        
    



    def process(self,path):
        data=[]
        mdict={}
        dict0={'a':0,'b':1}
        mdict[0]=dict0
        dict3={'u':4,'y':5,'l':6,'t':7}
        mdict[3]=dict3
        dict4={'g':8,'p':9,'gg':10}
        mdict[4]=dict4
        dict5={'c':11, 'd':12, 'cc':13, 'i':14, 'j':15, 'k':16,
               'm':17,'r':18, 'q':19, 'w':20, 'x':21, 'e':22, 'aa':23, 'ff':24}
        mdict[5]=dict5
        dict6={'v':25,'h':26,'bb':27,'j':28,'n':29,'z':30,'dd':31,'ff':32,'o':33}
        mdict[6]=dict6
        dict8={'t':35,'f':36}
        mdict[8]=dict8
        dict9={'t':37,'f':38}
        mdict[9]=dict9
        dict11={'t':40,'f':41}
        mdict[11]=dict11
        dict12={'g':42,'p':43,'s':44}
        mdict[12]=dict12
        dict14={1:2,2:3,7:34,10:39,13:45,14:46}
        mdict[14]=dict14
        
        f= open(path)
        for line in f:
            k=line.split(',')
            q=[0]*47
            for i in range(0,len(k)-1):
                if not((i==1) or (i==2) or (i==7) or (i==10) or
                 (i==13) or (i==14)):
                    temp=mdict[i]
                    q[temp[k[i]]]=1
                else:
                    temp=mdict[14]
                    q[temp[i]]=float(k[i])
                    
            data.append(q)

        return data


    def trainPredictValues(self,path):
        data=[]
        f= open(path)
        for line in f:
            k=line.split(',')
            k[-1]=k[-1].strip()
            data.append(k[-1])
        return data
        
    def getData(self):
        self.trainData=self.process(self.trainPath)
        self.trainDataPredict = self.trainPredictValues(self.trainPath)
        self.testData=self.process(self.testPath)
        self.testDataPredict = self.trainPredictValues(self.testPath)
        #self.testData=self.process(self.trainPath)
        

    def predict(self,n):

        k= knn.kNearestNeighbours()
        k.train(self.trainData,self.trainDataPredict)
        sol = k.test(self.testData,n)
        cor=0
        wrng=0
        print sol
        print self.testDataPredict
        for i in range(0,len(sol)):
            if sol[i]== self.testDataPredict[i]:
                cor=cor+1
            else:
                wrng = wrng +1
        print "for k=",n
        print 100*cor/len(sol)
        
        
        

    
