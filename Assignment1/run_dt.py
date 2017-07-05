import decisionTree as dt
import numpy as np
import sys


def main():
    depth = sys.argv[1]
    trainFile = sys.argv[2]
    testFile = sys.argv[3]
    rawData = getformattedData(trainFile)
    rawData = np.array(rawData)
    trainData = np.delete(rawData, np.s_[-1:], 1)
    trainLabel = np.delete(rawData, np.s_[0:-1], 1)

   # for test data
    rawTestData = getformattedData(testFile)
    rawTestData = np.array(rawTestData)
    testData = np.delete(rawTestData, np.s_[-1:], 1)
    testLabel = np.delete(rawTestData, np.s_[0:-1], 1)

    tree = dt.DecisionTree(trainData, trainLabel)
    tree.train()
    result = tree.test(testData, int(depth))
    tree.print_tree( tree.sol, 0, "")

    cnt =0
    rawTestData = getformattedData(testFile)
    k=open(testFile+"_Result","w")
    for line in rawTestData:
       # line = ''.join(line)
        line.append(str(result[cnt][0]))
        line = ','.join(line) + " \n"
        cnt=cnt+1
        k.write(line)
    k.close()
    c=0
    for i in range(0,len(result)):
        if result[i][0]==testLabel[i]:
            c=c+1
           # print result[i][0] + ": ",testLabel[i][0]
        #else:
            #print result[i][0] + ": ", testLabel[i][0]
    print float(c)/float(len(testLabel))

def getformattedData(file):
    f = open(file)
    badgesData = []
    for line in f:
        badgesData.append([str(x.strip()) for x in line.split(',')])
    f.close()
    return badgesData






if __name__=='__main__':
    main()