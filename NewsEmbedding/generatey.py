import numpy as np
import csv
import pandas as pd
import os
import json
import re
from convert_veracity_annotations import *





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

    rows = []
    i = 0
    for subdir, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith("annotation.json"):

                fpath = os.path.join(subdir, filename)
                print(os.path.join(subdir, filename))
                f = open(fpath, "r")
                dict = json.load(f)
                label = convert_annotations(dict, string=False)
                y[i] = label
                i += 1
                #dict['text'] = dict['text'].translate(str.maketrans('','', string.punctuation))

                rows.append(dict)

                #print(dict)
                #temp = pd.DataFrame.from_dict(dict)
                #print(temp['id'])
                #df = df.append(temp, ignore_index=True)
                #print(dict.keys())
                f.close()
    np.save(r'C:\Users\minim\PycharmProjects\SeniorPrj\results\y.npy', y)
    np.savetxt(r'C:\Users\minim\PycharmProjects\SeniorPrj\results\y.csv', y, delimiter=' ', newline='\n', fmt='%i')
    #f = open(path, "r")

    #f.close()

    return 0





readDB("charliehebdo")