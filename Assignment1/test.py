import process

def call():
    k=process.Process(r"C:\Seshasai\NEU_MSCS_Course\Spring2017\MachineLearning\materials\ps1\data\crx\crx.data.processed.training.txt",
                      r"C:\Seshasai\NEU_MSCS_Course\Spring2017\MachineLearning\materials\ps1\data\crx\crx.data.processed.testing")
    k.getData()

    predict = k.predict(10)

call()
    
