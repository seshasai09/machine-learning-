import driverForWinnow as dw
from os  import listdir

def run():
    a()
    b()
    c()


def a():
    n=1000
    for file in listdir(r"input/a/"):
        winnowWithoutMargin,winnowWithMargin = dw.driver("input/a/"+file,None,n)
        writeInstanceMistake(winnowWithoutMargin, r"output/a/WinnowWithoutMargin10of100of"+str(n)+".txt")
        writeInstanceMistake(winnowWithMargin, r"output/a/WinnowWithMargin10of100of" + str(n) + ".txt")
        n=n-500

def b():
    for file in listdir(r"input/b/"):
        k= file.split(".")
        k = int(k[0])
        winnowWithoutMargin,winnowWithMargin = dw.driver("input/b/"+file,None,k*40)
        writeInstanceMistake(winnowWithoutMargin, r"output/b/WinnowWithoutMargin10of20of"+str(k*40)+".txt")
        writeInstanceMistake(winnowWithMargin, r"output/b/WinnowWithMargin10of20of" + str(k*40) + ".txt")


def c():
    n=1000
    n10of100of1000 = "input/c/N10of100of1000.txt"
    n10of500of1000 = "input/c/N10of500of1000.txt"
    n10of1000of1000 = "input/c/N10of1000of1000.txt"
    c10of100of1000 = "input/c/C10of100of1000.txt"
    c10of500of1000 = "input/c/C10of500of1000.txt"
    c10of1000of1000 = "input/c/C10of1000of1000.txt"
    dw.driver( n10of100of1000,c10of100of1000,n)
    dw.driver(n10of500of1000, c10of500of1000, n)
    dw.driver(n10of1000of1000, c10of1000of1000, n)





def writeInstanceMistake(data,name):
    f = open(name,'w')
    for i in range(0,len(data[0])):
        f.write(str(data[0][i])+ ":" + str(data[1][i]) + "\n")

run()

