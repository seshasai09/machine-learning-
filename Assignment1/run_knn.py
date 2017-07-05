import process
import sys
import knn
import numpy as np


def main():
    k = sys.argv[1]
    trainFile = sys.argv[2]
    TestFile = sys.argv[3]
    if "crx" in trainFile:
        pro = process.Process(trainFile, TestFile)
        pro.getData()
        predict = pro.predict(int(k))
    else:
        processLensData(trainFile,TestFile,k)

def processLensData(trainFile,TestFile,k):
    f = open(trainFile)
    lensData = []
    for line in f:
        lensData.append([int(x.strip()) for x in line.split(',')])
    f.close()

    trainLabel = []
    f = open(trainFile)
    for line in f:
        n = line.split(',')
        n[-1] = n[-1].strip()
        trainLabel.append(n[-1])
    f.close()
   # trainLabel = np.delete(lensData, np.s_[0:-1], 1)
    trainData = np.delete(lensData, np.s_[-1:], 1)

    lensTestData = []
    f = open(TestFile)
    for line in f:
        lensTestData.append([int(x.strip()) for x in line.split(',')])
    f.close()

    testLabel = np.delete(lensTestData, np.s_[0:-1], 1)
    testData = np.delete(lensTestData, np.s_[-1:], 1)
    nn = knn.kNearestNeighbours()
    nn.train(trainData,trainLabel)
    sol =nn.test(testData, int(k))
    cor = 0
    wrng = 0
    print sol
    for i in range(0, len(sol)):
        print sol[i]
        print testLabel[i][0]
        if int(sol[i]) == (testLabel[i][0]):
            cor = cor + 1
        else:
            wrng = wrng + 1
    print "for k=", sol
    print 100 * cor / len(sol)




if __name__=='__main__':
    main()