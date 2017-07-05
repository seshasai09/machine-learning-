import driverForPerceptron as dp
from os  import listdir


def run():
    a()
    b()
    c()


def a():
    n=1000
    for file in listdir(r"input/a/"):
        perceptronWithoutMargin,perceptronWithMargin = dp.driver("input/b/"+file,None,n)
        writeInstanceMistake(perceptronWithoutMargin, r"output/a/PerceptronWithoutMargin10of100of"+str(n)+".txt")
        writeInstanceMistake(perceptronWithMargin, r"output/a/PerceptronWithMargin10of100of" + str(n) + ".txt")
        n=n-500

def b():
    n=40
    for file in listdir(r"input/b/"):
        k=file.split(".")
        k=int(k[0])
        perceptronWithoutMargin, perceptronWithMargin = dp.driver("input/b/"+file,None,k*40)
        writeInstanceMistake(perceptronWithoutMargin, r"output/b/PerceptronWithoutMargin10of20of"+str(k*40)+".txt")
        writeInstanceMistake(perceptronWithMargin, r"output/b/PerceptronWithMargin10of20of" + str(k*40) + ".txt")

def c():
    n=1000
    n10of100of1000 = "input/c/N10of100of1000.txt"
    n10of500of1000 = "input/c/N10of500of1000.txt"
    n10of1000of1000 = "input/c/N10of1000of1000.txt"
    c10of100of1000 = "input/c/C10of100of1000.txt"
    c10of500of1000 = "input/c/C10of500of1000.txt"
    c10of1000of1000 = "input/c/C10of1000of1000.txt"
    dp.driver( n10of100of1000,c10of100of1000,n)
    dp.driver(n10of500of1000, c10of500of1000, n)
    dp.driver(n10of1000of1000, c10of1000of1000, n)





def writeInstanceMistake(data,name):
    f = open(name,'w')
    for i in range(0,len(data[0])):
        f.write(str(data[0][i])+ ":" + str(data[1][i]) + "\n")

run()

