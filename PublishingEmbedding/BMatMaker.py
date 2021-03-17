import numpy as np
import pandas as pd
import csv



def makeRealB(file):
    df = pd.read_csv(file, header=0)
    #print(df)
    P = df["publisher"].to_numpy()
    A = df['news'].to_numpy()
    pubs, arts = [], []
    pind, aind = [], []
    #print(df.iloc[0][1])
    for i in range(len(P)):
        if P[i] not in pubs:
            pubs.append(P[i])
            pind.append(i)
        if A[i] not in arts:
            arts.append(A[i])
            aind.append(i)
        #print(pubs, arts)
    #B = [[x[:]]][]
    l = len(pubs)
    n = len(arts)
    print(l)
    B = np.zeros((l, n), dtype=np.longdouble)
    print(len(B), len(B[0]))
    for i in range(l):
        for j in range(n):
            #print(j, df.iloc[i][1], arts[j])
            if df.iloc[pind[i], 0] == df.iloc[aind[j], 0]:
                #print("match!!!! at ", str(i), " ", str(j))
                B[i, j] = 1
    np.save('C:\\Users\\minim\\PycharmProjects\\SeniorPrj\\results\\B.npy', B)


    #print(B)
    with open('../PublishingEmbedding/Bmat.csv', 'w', encoding="utf-8", newline='\n') as f:
        writer = csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL, )
        writer.writerows(B)
                #print(len(pubs), len(arts))
        #if publisher not in list P
            #add publisher to list P
        #if article not in list A
            #add article to list A
        #also have list of publisher articles AP,
        #go through lists P and A, if Pi published Aj, set Bij to 1, else 0
    #normalize/indicize publishers and articles
    #dictionary of publishers with articles they have posted.


makeRealB("publisher-news.csv")