def test():
    f = open("sol.txt")
    p=[]
    q=[]
    for i in f:
        k=i.split(",")
        k=k.spl
        print k
        for i in range(len(k)):
            if i%2==0:
                p.append(k[i]+"\n")
            else:
                q.append(k[i] + "\n")

    w=open("val.txt",'w')

    for i in range(len(p)):
        w.write(p[i]+"\n")

    w = open("trai.txt", 'w')

    for i in range(len(q)):
        w.write(q[i] + "\n")





test()