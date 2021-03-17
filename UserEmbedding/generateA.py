import csv
import pandas as pd
import numpy as np
import os
from ordered_set import OrderedSet as oset
import matplotlib.pyplot as plt


A = np.zeros((19867, 19867), dtype=np.int8) #19906

U = np.load('C:\\Users\\minim\\PycharmProjects\\SeniorPrj\\results\\users.npy')
U = np.unique(U)

print(len(U))
def readDB(database):

    origpath = "C:\\Users\\minim\\OneDrive\\Desktop\\pheme rumors\\pheme-rumour-scheme-dataset\\threads\\en\\"
    path = "{opath}{db}".format(opath=origpath, db=database)
    cols = ['contributors', 'truncated', 'text', 'in_reply_to_status_id', 'id', 'favorite_count',
                               'source', 'retweeted', 'coordinates', 'entities', 'in_reply_to_screen_name', 'id_str',
                               'retweet_count', 'in_reply_to_user_id', 'favorited', 'user', 'geo',
                               'in_reply_to_user_id_str', 'possibly_sensitive', 'lang', 'created_at', 'filter_level',
                               'in_reply_to_status_id_str', 'place', 'metadata', 'extended_entities']
    df = pd.DataFrame(columns=cols)



    ua = oset()
    t = oset()
    u = oset()
    for subdir, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith("who-follows-whom.dat"):
                fpath = os.path.join(subdir, filename)
                arr = np.loadtxt(fpath, dtype=np.longdouble)
                for item in arr:
                    #print(item)

                    u.add((item[0], item[1]))
                    t.add((item[0], item[1]))
                    #ua.add(item[0])
                    #ub.add(item[1])
    print('-'*50, '\n')
    while len(u) > 0:
        it = u.pop()
        #print(testa, testb)
        if it[0] in U and it[1] in U:
        #if(it[0] in U):
            if (it[1], it[0]) in t:
                print((it[1], it[0]), (it[1], it[0]) in t)
                i = np.where(U == it[0])[0][0]
            #if(it[1] in U):
                j = np.where(U == it[1])[0][0]
                A[i, j] = 1

             #   j = np.where(U == it[0])[0][0]
        #elif(it[1] in U):
           # i = j = np.where(U == it[1])[0][0]
        else:
            pass

        #print(i, j)
        #A[i, j] = 1

    for i in range(19867):
        A[i, i] = 0
    print(A.sum())
    np.save('C:\\Users\\minim\\PycharmProjects\\SeniorPrj\\results\\A.npy', A)
    #p = plt.imshow(A)
    #plt.show()
    return 0









readDB("charliehebdo")