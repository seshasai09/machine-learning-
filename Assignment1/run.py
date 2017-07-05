import decisionTree as dt
import numpy as np

def run(inputFile,outputFile):


    #lenses data set
##    f = open(r"C:\Seshasai\NEU_MSCS_Course\Spring2017\MachineLearning\materials\ps1\data\lenses\lenses.training")
##    data=[]
##    for line in f:
##        data.append([int(x) for x in line.split(',')])
##    
##    k=np.array(data)
##    label=np.delete(k,np.s_[0:4],1)
##    data = np.delete(k,np.s_[4:],1)
##    tree = dt.DecisionTree(data,label)
##    tree.train()
##    f = open(r"C:\Seshasai\NEU_MSCS_Course\Spring2017\MachineLearning\materials\ps1\data\lenses\lenses.testing")
##    testData=[]
##    for line in f:
##        testData.append([int(x) for x in line.split(',')])
##    
##    k=np.array(testData)
##    label=np.delete(k,np.s_[0:4],1)
##    data = np.delete(k,np.s_[4:],1)
##    print tree.test(testData)
    #tree.print_tree(tree.sol)

    #Badges data set
    f=open(inputFile)
    badgesData=[]
    for line in f:
        badgesData.append([str(x.strip()) for x in line.split(' ')])
    badgesData=np.array(badgesData)
    label = np.delete(badgesData,np.s_[1:],1)
    data=np.delete(badgesData,np.s_[0:1],1)
    dictAlpha={}
    for i in range(0,26):
        dictAlpha[chr(i+97)]=i
    dictAlpha[' ']=26
    a = np.zeros((len(data),20))

    for i in range (0,len(a)):
        fill1(a,i,data[i][0],dictAlpha)
        fill2(a,i,data[i][1],dictAlpha)
    #print a[0]
    outputF = open(outputFile, 'w')
    for i in range(0, len(a)):
        p = ','.join(map(str, a[i]))
        p = p + "," + str(label[i][0])
        outputF.write(p + "\n")
    outputF.close()
    print "writing file to output"
    tree = dt.DecisionTree(a,label)
    tree.train()
    #tree.print_tree(tree.sol,0)
    ### testing the badges data set
    f = open(r"C:\Seshasai\NEU_MSCS_Course\Spring2017\MachineLearning\materials\ps1\data\badges\badges.testing")
    testData=[]
    for line in f:
        testData.append([str(x.strip()) for x in line.split(' ')])
    testData=np.array(testData)
    label = np.delete(testData,np.s_[1:],1)
    data=np.delete(testData,np.s_[0:1],1)
    a = np.zeros((len(data),20))

    for i in range (0,len(a)):
        fill1(a,i,data[i][0],dictAlpha)
        fill2(a,i,data[i][1],dictAlpha)
    #print a
    k= tree.test(a,7)
    #print k
    cnt=0
    print len(label)
    print len(k)
    for i in range(0,len(k)):
        if k[i]==label[i]:
            cnt=cnt+1
            print k[i] + ": ",label[i]
    print float(cnt)/float(len(label))
            
                           
                                  
def fill1(a,i,k,dictAlpha):
    if len(k)>10:
        for z in range(0,10):
            a[i][z]=dictAlpha[k[z]]

    else:
        for z in range(0,len(k)):
            a[i][z]=dictAlpha[k[z]]
        for z in range(len(k),10):
            a[i][z]=dictAlpha[' ']

def fill2(a,i,k,dictAlpha):
    if len(k)>10:
        for z in range(10,20):
            a[i][z]=dictAlpha[k[z-10]]

    else:
        for z in range(10,10+len(k)):
            a[i][z]=dictAlpha[k[z-10]]
        for z in range(10+len(k),20):
            a[i][z]=dictAlpha[' ']
    

                                
                                  
                                  

    
#run()
