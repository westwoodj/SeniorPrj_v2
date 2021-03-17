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

def class_value(classV):

    if classV == 'VERY HIGH':
        return 5
    elif classV == 'HIGH':
        return 4
    elif classV == 'MOSTLY FACTUAL':
        return 3
    elif classV == 'MIXED':
        return 2
    elif classV == 'LOW':
        return 1
    else:
        return 0



#url ex. is str '
def getCred(uurl, name, df):
    cred, eVal = 0, 0

    if df['site_name'].str.contains(name).any():
        Series = df['site_name'].str.contains(name, regex=False)
        eVal = 1
        cred = df.at[Series[Series == True].index[0], 'factual_reporting_rating']
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
                cred = df.at[Series[Series == True].index[0], 'factual_reporting_rating']
                eVal = 1
            elif df['url'].str.contains(expanded_url, regex=False).any():
                eVal = 1
                cred = df.loc[expanded_url]['factual_reporting_rating']
            else:
                cred = 0
                eVal = 0
        else:
            cred = 0
            eVal = 0

    print("cred: ", cred," eVal: ", eVal)

    #print(expanded_url)

    return cred, eVal


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
    biasData['factual_reporting_rating'] = biasData['factual_reporting_rating'].apply(class_value)
    #print(biasData.head)
    origpath = "C:\\Users\\minim\\OneDrive\\Desktop\\pheme rumors\\pheme-rumour-scheme-dataset\\threads\\en\\"

    path = "{opath}{db}".format(opath=origpath, db=database)

    cols = ['contributors', 'truncated', 'text', 'in_reply_to_status_id', 'id', 'favorite_count',
            'source', 'retweeted', 'coordinates', 'entities', 'in_reply_to_screen_name', 'id_str',
            'retweet_count', 'in_reply_to_user_id', 'favorited', 'user', 'geo',
            'in_reply_to_user_id_str', 'possibly_sensitive', 'lang', 'created_at', 'filter_level',
            'in_reply_to_status_id_str', 'place', 'metadata', 'extended_entities']

    df = pd.DataFrame(columns=cols)


    creds = {}
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
                        bias, eVal = getCred(url, name, biasData)

                    else:
                        bias = 0
                        eVal = 0
                    # dict['text'] = dict['text'].translate(str.maketrans('','', string.punctuation))

                    append_value(creds, dict['user']['id'], bias)
                    append_value(eVals, dict['user']['id'], eVal)

                    # print(dict)
                    # temp = pd.DataFrame.from_dict(dict)
                    # print(temp['id'])
                    # df = df.append(temp, ignore_index=True)
                    # print(dict.keys())
                    f.close()
    c = np.asarray(list(creds.values()))
    #e = np.asarray(list(eVals.values()))
    #print(o, e)
    np.save('C:\\Users\\minim\\PycharmProjects\\SeniorPrj\\PublishingEmbedding\\c.npy', c)
    #np.save('C:\\Users\\minim\\PycharmProjects\\SeniorPrj\\PublishingEmbedding\\e.npy', e)
'''
    with open("o.csv", 'w', newline='') as csvf:
        writer = csv.DictWriter(csvf, fieldnames=['publisher_id', 'bias'], quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for key, value in biases.items():
            writer.writerow({'publisher_id': key,'bias': value})
    print(biases)
'''
#f = open(path, "r")

#f.close()




# data is

readLinks("charliehebdo")