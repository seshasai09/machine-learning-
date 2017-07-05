import decisionTree as dt
import numpy as np

def run(inputFile,outputFile):

    #f=open(r"C:\Seshasai\NEU_MSCS_Course\Spring2017\MachineLearning\materials\ps1\data\badges\badges.training")
    f=open(inputFile)
    badgesData=[]
    for line in f:
        badgesData.append([str(x.strip()) for x in line.split(' ')])
    f.close()
    badgesData=np.array(badgesData)
    label = np.delete(badgesData,np.s_[1:],1)
    data=np.delete(badgesData,np.s_[0:1],1)
    dictAlpha={}
    for i in range(0,26):
        dictAlpha[chr(i+97)]=i
    dictAlpha[' ']=26
    a = np.zeros((len(badgesData),540))
   # print a

    for i in range (0, len(a)):
        data[i][0]
        data[i][1]
        fill(a,i,data[i][0],data[i][1],dictAlpha)

    outputF = open(outputFile,'w')
    for i in range(0,len(a)):
        p=','.join(map(str,a[i]))
        p= p + "," + str(label[i][0])
        outputF.write(p+"\n")
    outputF.close()
    print "writing file to output"
    tree = dt.DecisionTree(a,label)
    tree.train()

    f=open(r"C:\Seshasai\NEU_MSCS_Course\Spring2017\MachineLearning\materials\ps1\data\badges\badges.testing")
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
    a = np.zeros((len(badgesData),540))
   # print a

    for i in range (0, len(a)):
        data[i][0]
        data[i][1]
        fill(a,i,data[i][0],data[i][1],dictAlpha)

    print "binary tree"
    tree.print_tree(tree.sol,0,"")
    k= tree.test(a,12)
    cnt=0
    for i in range(0,len(k)):
        if k[i]==label[i]:
            cnt=cnt+1
            print k[i] + ": ",label[i]
    print float(cnt)/float(len(label))
    

def fill(a,i,str1,str2,dictAlpha):

    if len(str1)>10:
        for z in range(0,10):
            k=dictAlpha[str1[z]]
            a[i][27*z + k]=1
    else:
        for z in range (0, len(str1)):
            k=dictAlpha[str1[z]]
            a[i][27*z + k]=1
        for z in range(len(str1),10):
            a[i][27*z + 26]=1

    if len(str2)>10:
        for z in range(10,20):
            k=dictAlpha[str2[z-10]]
            a[i][27*z + k]=1
    else:
        for z in range (10,len(str2)+10):
            k=dictAlpha[str2[z-10]]
            a[i][27*z + k]=1
        for z in range(10+len(str2),20):
            a[i][27*z + 26]=1
            

#run("badges.training","badges.training.bs")
    
    
