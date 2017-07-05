
from os  import listdir
import numpy as np
import matplotlib.pyplot as plt

minThreshold=[]
dict={}


# this fucntion find the value for number of survives using binary search.
# Once the optimal S value is the function uses it to plot the curve for question partc b of the questions
def driverForThhreshold():

    for file in listdir(r"output/b"):
        maxThresold =[]
        f = open(r"output/b/"+file)
        lis = []
        for line in f:
            line = line.split(":")
            lis.append(int(line[0]))
        findThreshold(lis,0,1000,maxThresold)
        minThreshold.append(max(maxThresold))

    findMistake (min(minThreshold))


def findThreshold(lis,min,max,maxThresold):
    found = False

    for i in range(1,len(lis)):
        k = lis[i] - lis[i-1]
        if(k > max):
            found =True
            maxThresold.append(k)

    if not found:
       k= findThreshold(lis,min,(min+max)/2,maxThresold)
       if not k:
           y= findThreshold(lis,(min+max)/2,max,maxThresold)
    return k




def findMistake(S):

    for file in listdir(r"output/b/"):

        f = open(r"output/b/"+file)
        instances = []
        mistakes=[]
        for line in f:
            line = line.split(":")
            instances.append(int(line[0]))
            mistakes.append(int(line[1]))
        m=findMistakes(instances,mistakes,S)
        dict[file]=m
        newDict={}
    X_axis=[40,80,120,160,200]
    prefix = ["Perceptron","Winnow"]
    suffix = ["WithMargin","WithoutMargin"]
    someDict={}
    for i in range(0,5):
        someDict[i]=[]
    count =0

    for x in prefix:
        for y in suffix:
            for i in X_axis:
                for k in dict:
                    if x in k and y in k and str(i) in k:
                        p= dict[k]
                        tempLis= someDict[count]
                        tempLis.append(p)
            count = count + 1





    plt.plot(X_axis,someDict[0],"b",label="perceptronWithMargin")
    plt.plot(X_axis,someDict[1],"g",label="perceptronWithoutMargin")
    plt.plot(X_axis,someDict[2],"c",label="winnowWithoutMargin")
    plt.plot(X_axis,someDict[3],"m",label="winnowWithMargin")
    #plt.plot(X_axis,someDict[4],"oy")
    plt.legend()
    plt.ylabel("Mistakes")
    plt.xlabel("n")
    plt.show()


def findMistakes(instances,mistakes,S):
    for i in range(1,len(instances)):
        if instances[i]-instances[i-1]>=S:
            return mistakes[i]



driverForThhreshold()

