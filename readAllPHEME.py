import csv
import pandas as pd
import json
import os
import re
from convert_veracity_annotations import *
import numpy as np
from ordered_set import OrderedSet as oset


'''
for every thread -
    walk each file
        read the annotation file
            if annotation != 0
                write source tweet to source tweet
                write who follows whom to users shit
                write retweets from retweets file
            else
                write to testing data -- unclassified tweets

'''

def readDB(database):

    origpath = "C:\\Users\\minim\\OneDrive\\Desktop\\pheme rumors\\pheme-rumour-scheme-dataset\\threads\\en\\"
    path = "{opath}{db}".format(opath=origpath, db=database)
    cols = ['contributors', 'truncated', 'text', 'in_reply_to_status_id', 'id', 'favorite_count',
                               'source', 'retweeted', 'coordinates', 'entities', 'in_reply_to_screen_name', 'id_str',
                               'retweet_count', 'in_reply_to_user_id', 'favorited', 'user', 'geo',
                               'in_reply_to_user_id_str', 'possibly_sensitive', 'lang', 'created_at', 'filter_level',
                               'in_reply_to_status_id_str', 'place', 'metadata', 'extended_entities']
    df = pd.DataFrame(columns=cols)
    y = np.zeros(74)

    tweets = []
    user_news = []
    i = 0
    t = oset()
    u = oset()
    for subdir, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith("annotation.json"):
                fpath = os.path.join(subdir, filename)
                print(os.path.join(subdir, filename))
                f = open(fpath, "r")
                dict = json.load(f)
                label = convert_annotations(dict, string=False)
                if label != 0:
                    y[i] = label
                    i += 1
                    # dict['text'] = dict['text'].translate(str.maketrans('','', string.punctuation))
                    # rows.append(dict)
                    # print(dict)
                    # temp = pd.DataFrame.from_dict(dict)
                    # print(temp['id'])
                    # df = df.append(temp, ignore_index=True)
                    # print(dict.keys())
                    f.close()
                    if filename.endswith(".json"):
                        if "source-tweets" in subdir:  # or "reactions" in subdir
                            fpath = os.path.join(subdir, filename)
                            print(os.path.join(subdir, filename))
                            f = open(fpath, "r")
                            dict = json.load(f)
                            dict['text'] = re.sub(r"[\n\t]*", "", dict['text'])
                            # dict['text'] = dict['text'].translate(str.maketrans('','', string.punctuation))

                            tweets.append(dict)

                            # print(dict)
                            # temp = pd.DataFrame.from_dict(dict)
                            # print(temp['id'])
                            # df = df.append(temp, ignore_index=True)
                            # print(dict.keys())
                            f.close()

                            # NEED TO SAVE TO source-tweets.csv at end

                        if filename.endswith("retweets.json"):

                            fpath = os.path.join(subdir, filename)
                            # print(os.path.join(subdir, filename))
                            f = open(fpath, "r")
                            for line in f:
                                dict = json.loads(line)
                                # print(dict['user']['id'], dict['retweeted_status']['id'])
                                towrite = {'id': dict['user']['id'], 'tweet-id-rtd': dict['retweeted_status']['id']}
                                user_news.append(towrite)
                            # dict = json.load(f)
                            # dict['text'] = re.sub(r"[\n\t]*", "", dict['text'])
                            # dict['text'] = dict['text'].translate(str.maketrans('','', string.punctuation))
                            # print(dict['user']['id'], dict['media']['id_str'])
                            # rows.append(dict['user']['id'])

                            # print(dict)
                            # temp = pd.DataFrame.from_dict(dict)
                            # print(temp['id'])
                            # df = df.append(temp, ignore_index=True)
                            # print(dict.keys())
                            f.close()
            if filename.endswith("who-follows-whom.dat"):
                fpath = os.path.join(subdir, filename)
                arr = np.loadtxt(fpath, dtype=np.longdouble)
                for item in arr:
                    #print(item)

                    u.add((item[0], item[1]))
                    t.add((item[0], item[1]))
                    #ua.add(item[0])
                    #ub.add(item[1])




    with open("source_tweets.csv", 'w', encoding="utf-8", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=cols)
        writer.writeheader()
        rows = []
        for subdir, dirs, files in os.walk(path):
            for filename in files:
                if filename.endswith(".json"):
                    if "source-tweets" in subdir: #or "reactions" in subdir
                        fpath = os.path.join(subdir, filename)
                        print(os.path.join(subdir, filename))
                        f = open(fpath, "r")
                        dict = json.load(f)
                        dict['text'] = re.sub(r"[\n\t]*", "", dict['text'])
                        #dict['text'] = dict['text'].translate(str.maketrans('','', string.punctuation))

                        rows.append(dict)

                        #print(dict)
                        #temp = pd.DataFrame.from_dict(dict)
                        #print(temp['id'])
                        #df = df.append(temp, ignore_index=True)
                        #print(dict.keys())
                        f.close()
        writer.writerows(rows)
    csvfile.close()


    #f = open(path, "r")

    #f.close()

    return 0






"""

for making A with u and t
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

"""



if __name__ == "__main__":
    readDB("charliehebdo")