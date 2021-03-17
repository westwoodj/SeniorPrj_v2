import pandas as pd
import csv
import numpy as np
from sklearn.decomposition import NMF
import ast
import os
import re
import json
import requests
from urllib.parse import urlparse

#np.save(r'C:\Users\学汪\Desktop\summner research\kaggle_data\X.npy',X_news)




#url ex. is str '
def getBias(uurl, name, df):
    bias, eVal = 0, 0

    if df['site_name'].str.contains(name).any():
        Series = df['site_name'].str.contains(name, regex=False)
        eVal = 1
        bias = df.at[Series[Series == True].index[0], 'bias_rating']
    else:
        try:
            expanded_url = requests.head(uurl, allow_redirects=True, timeout=5).url
        except Exception as e:
            expanded_url = uurl
            return 0, 0
        if expanded_url != "None":
            o = urlparse(expanded_url)
            #print("netloc is: ", o.netloc)
            if df['url'].str.contains(o.netloc, regex=False).any():
                Series = df['url'].str.contains(o.netloc, regex=False)
                #print(Series[Series == True].index[0])
                bias = df.at[Series[Series == True].index[0], 'bias_rating']
                eVal = 1
            elif df['url'].str.contains(expanded_url, regex=False).any():
                eVal = 1
                bias = df.loc[expanded_url]['bias_rating']
            else:
                bias = 0
                eVal = 0
        else:
            bias = 0
            eVal = 0

    print("bias: ", bias," eVal: ", eVal)

    #print(expanded_url)

    return bias, eVal


def append_value(dict_obj, key, value):
    # Check if key exist in dict or not
    if key in dict_obj:
        # Key exist in dict.
        # Check if type of value of key is list or not
        pass
        #dict_obj[key].append(value)
    else:
        # As key is not in dict,
        # so, add key-value pair
        dict_obj[key] = value


def readLinks(database):


    biasData = pd.read_csv("media-bias-scrubbed-results.csv", header=0)
    #i = df['url']
    biasData.set_index(biasData['url'])
    #print(biasData.head)
    origpath = "C:\\Users\\minim\\OneDrive\\Desktop\\pheme rumors\\pheme-rumour-scheme-dataset\\threads\\en\\"

    path = "{opath}{db}".format(opath=origpath, db=database)

    cols = ['contributors', 'truncated', 'text', 'in_reply_to_status_id', 'id', 'favorite_count',
            'source', 'retweeted', 'coordinates', 'entities', 'in_reply_to_screen_name', 'id_str',
            'retweet_count', 'in_reply_to_user_id', 'favorited', 'user', 'geo',
            'in_reply_to_user_id_str', 'possibly_sensitive', 'lang', 'created_at', 'filter_level',
            'in_reply_to_status_id_str', 'place', 'metadata', 'extended_entities']

    df = pd.DataFrame(columns=cols)


    biases = {}
    eVals = {}
    for subdir, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith(".json"):
                if "source-tweets" in subdir:  # or "reactions" in subdir
                    fpath = os.path.join(subdir, filename)
                    #print(os.path.join(subdir, filename))
                    f = open(fpath, "r")
                    dict = json.load(f)
                    name = dict['user']['name']
                    #print(name)
                    url = dict['user']['url']
                    #print(url)
                    pubid = dict['user']['id']
                    if url != 'None':
                        bias, eVal = getBias(url, name, biasData)

                    else:
                        bias = 0
                        eVal = 0
                    # dict['text'] = dict['text'].translate(str.maketrans('','', string.punctuation))

                    append_value(biases, dict['user']['id'], bias)
                    append_value(eVals, dict['user']['id'], eVal)

                    # print(dict)
                    # temp = pd.DataFrame.from_dict(dict)
                    # print(temp['id'])
                    # df = df.append(temp, ignore_index=True)
                    # print(dict.keys())
                    f.close()
    o = np.asarray(list(biases.values()), dtype=np.longdouble)
    e = np.asarray(list(eVals.values()), dtype=np.longdouble)
    #print(o, e)
    np.save('C:\\Users\\minim\\PycharmProjects\\SeniorPrj\\results\\o.npy', o)
    np.save('C:\\Users\\minim\\PycharmProjects\\SeniorPrj\\results\\e.npy', e)

    with open("o.csv", 'w', newline='') as csvf:
        writer = csv.DictWriter(csvf, fieldnames=['publisher_id', 'bias'], quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for key, value in biases.items():
            writer.writerow({'publisher_id': key,'bias': value})
    print(biases)
#f = open(path, "r")

#f.close()




# data is

readLinks("charliehebdo")




