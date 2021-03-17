import numpy as np
import csv
import pandas as pd


def append_value(dict_obj, key, value):
    # Check if key exist in dict or not
    if key in dict_obj:
        # Key exist in dict.
        # Check if type of value of key is list or not
        if not isinstance(dict_obj[key], list):
            # If type is not list then make it list
            dict_obj[key] = [dict_obj[key]]
        # Append the value in list
        dict_obj[key].append(value)
    else:
        # As key is not in dict,
        # so, add key-value pair
        dict_obj[key] = value

def makeW(file):
    df = pd.read_csv(file, header=0)
    #print(df.head)
    U, A = [], []
    Uind, Aind = [], []

    Wdict = {}
    for index, row in df.iterrows():

        append_value(Wdict, row['id'], row['tweet-id-rtd'])
        #else:
            #print("user {user} has retweeted multiple tweets. at index {index}".format(user=row['id'], index=index))

        if row['id'] not in U:
            U.append(row['id'])
            Uind.append(index)

        if row['tweet-id-rtd'] not in A:
            A.append(row['tweet-id-rtd'])
            Aind.append(index)


    unp = np.asarray(U, dtype=np.longdouble)
    anp = np.asarray(A, dtype=np.longdouble)

    np.save('C:\\Users\\minim\\PycharmProjects\\SeniorPrj\\InteractionEmbedding\\users.npy', unp)
    np.save('C:\\Users\\minim\\PycharmProjects\\SeniorPrj\\InteractionEmbedding\\news.npy', anp)
    #with open("users.csv", 'w', encoding="utf-8", newline='\n') as usf: #write set U for later use
    #    wr = csv.writer(usf, quoting=csv.QUOTE_ALL)
    #    wr.writerow(U)
    #with open("news.csv", 'w', encoding="utf-8", newline='\n') as nf: #write set A for later use
    #    wr = csv.writer(nf, quoting=csv.QUOTE_ALL)
    #   wr.writerow(A)

    #print(Uind, Aind)
    m: int = 19867 #len(U)
    n: int = 74 #len(A)
    #print(m, n)

    W = np.zeros((m, n), dtype=np.longdouble)


    for i in range(m):
        for j in range(n):
            #print(Wdict[U[i]])
            if isinstance(Wdict[U[i]], list):
                if A[j] in Wdict[U[i]]:
                    #print("retweet!")
                    W[i, j] = 1
            else:
                if A[j] == Wdict[U[i]]:
                    W[i, j] = 1


    '''
    for i in range(m):
        for j in range(n):
            #print(i, j)
            #print(df.iloc[i, 1], A[j])
            if df.iloc[i, 1] == A[j]:
                W[i, j] = 1
    '''
    np.save('C:\\Users\\minim\\PycharmProjects\\SeniorPrj\\results\\W.npy', W)

    with open('Wmat.csv', 'w', encoding="utf-8", newline='\n') as f:
        writer = csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL, )
        writer.writerows(W)



makeW("user-news.csv")