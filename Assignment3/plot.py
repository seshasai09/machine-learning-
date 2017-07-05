import numpy as np
import matplotlib.pyplot as plt

# this function plots the graph for mistakes as a function of number if instances
# use matplotlib to plot the graphs.  This function plotts two graphs one for
# number of attributes =500 and when number of attributes=1000
def readAndPlot():
    getPlotFor1000()
    getPlotFor500()

def getPlotFor1000():
    fname = r"output\a\PerceptronWithMargin10of100of1000.txt"

    percpWithMargin1000errorCount, percpWithMargin1000instances = getData(fname)

    fname = r"output\a\PerceptronWithoutMargin10of100of1000.txt"
    percpWithoutMargin1000errorCount, percpWithoutMargin1000instances = getData(fname)

    fname = r"output\a\WinnowWithMargin10of100of1000.txt"

    winnowWithMargin1000errorCount, winnowWithMarginMargin1000instances = getData(fname)
    fname = r"output\a\WinnowWithoutMargin10of100of1000.txt"

    winnowWithoutMargin1000errorCount, winnowWithoutMarginMargin1000instances = getData(fname)
    plt.plot(percpWithMargin1000instances, percpWithMargin1000errorCount, label="perceptronWithMargin")
    plt.plot(percpWithoutMargin1000instances, percpWithoutMargin1000errorCount, label="perceptronWithoutMargin")
    plt.plot(winnowWithMarginMargin1000instances, winnowWithMargin1000errorCount, label="winnowWithMargin")
    plt.plot(winnowWithoutMarginMargin1000instances, winnowWithoutMargin1000errorCount, label="winnowWithoutMargin")
    plt.legend()
    plt.ylabel("Mistakes")
    plt.xlabel("n=1000")

    plt.show()

def getPlotFor500():
    fname = r"output\a\PerceptronWithMargin10of100of500.txt"

    percpWithMargin500errorCount, percpWithMargin500instances = getData(fname)

    fname = r"output\a\PerceptronWithoutMargin10of100of500.txt"
    percpWithoutMargin500errorCount, percpWithoutMargin500instances = getData(fname)

    fname = r"output\a\WinnowWithMargin10of100of500.txt"

    winnowWithMargin500errorCount, winnowWithMarginMargin500instances = getData(fname)
    fname = r"output\a\WinnowWithoutMargin10of100of500.txt"

    winnowWithoutMargin500errorCount, winnowWithoutMarginMargin500instances = getData(fname)

    plt.plot(percpWithMargin500instances, percpWithMargin500errorCount,label="perceptronWithMargin")
    plt.plot(percpWithoutMargin500instances, percpWithoutMargin500errorCount,label="perceptronWithoutMargin")
    plt.plot(winnowWithMarginMargin500instances, winnowWithMargin500errorCount,label="winnowWithMargin")
    plt.plot(winnowWithoutMarginMargin500instances, winnowWithoutMargin500errorCount,label="winnowWithoutMargin")
    #plt.legend(bbox_to_anchor=(0.2,.95),loc=2,boarderaxespad=0.1)
    plt.legend()
    plt.ylabel("Mistakes")
    plt.xlabel("n=500")
    plt.show()


def getData(fileName):
    f = open(fileName)
    listErrorCount = []
    listInstances = []
    for line in f:
        line = line.split(":")
        listInstances.append(line[0])
        listErrorCount.append(line[1])
    return np.array(listErrorCount), np.array(listInstances)


readAndPlot()
