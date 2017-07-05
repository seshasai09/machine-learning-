import MultinomialNaiveBayes

def run():
    f= open(r"data\train-files.txt")

    classes=[line.split("/")[0] for line in f.readlines()] # taking only the class names
    f.close()
    classData={} # hashmap with key as class and value as taining file for the class
    for cla in classes:
        classData[cla]="data" +"\\"+cla+".train.txt"

    f=open(r"data\vocabulary.txt")
    data=[] # datastructure to load all the words from vocabulary.txt file. We ignore the counts
    data = [line.split(" ")[0] for line in f.readlines()]
    f.close()

    #initializing the naive bayes model
    model = MultinomialNaiveBayes.NaiveBayes(classes,classData,data)
    testFile=open(r"data\test.txt")
    rawTestData = [line.strip("\n").split(" ")  for line in testFile.readlines()]

    testData=[]# data structure that has test data
    # data structure that has actual labels for the test data.
    # These values are extracted from the first column of test file
    actualVal=[]
    for row in rawTestData:
        k=row[5:]
        p=row[1:4]
        testData.append(p+k)
        actualVal.append(row[0:1])

    model.train()
    ans = model.test(testData)

    printSolToFile(ans)


def printSolToFile(ans):
    solFile=open(r"output\predictions.nb",'w')
    for i in range(0,len(ans)):
        if(ans[i] == ARTICLES):
            solFile.write(ONE + NEWLINE)
        elif (ans[i] == CORPORATE):
            solFile.write(TWO + NEWLINE)
        elif(ans[i] == ENRON_T_S):
            solFile.write(THREE + NEWLINE)
        elif(ans[i] == ENRON_TRAVEL_CLUB):
            solFile.write(FOUR + NEWLINE)
        elif(ans[i]== HEA_NESA):
            solFile.write(FIVE + NEWLINE)
        elif(ans[i]== PERSONAL):
            solFile.write(SIX + NEWLINE)
        elif(ans[i]== SYSTEMS):
            solFile.write(SEVEN + NEWLINE)
        else:
            solFile.write(EIGHT + "\n")

#constants
ARTICLES="articles"
CORPORATE="corporate"
ENRON_T_S="enron_t_s"
ENRON_TRAVEL_CLUB="enron_travel_club"
HEA_NESA="hea_nesa"
PERSONAL="personal"
SYSTEMS="systems"
ONE = "1.0"
TWO = "2.0"
THREE = "3.0"
FOUR = "4.0"
FIVE = "5.0"
SIX = "6.0"
SEVEN = "7.0"
EIGHT = "8.0"
NEWLINE="\n"


if __name__ == "__main__":
    run()