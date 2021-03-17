import pandas as pd
import numpy as np
import json
import os
import re
import csv


def readRetweets(database):
    origpath = "C:\\Users\\minim\\OneDrive\\Desktop\\pheme rumors\\pheme-rumour-scheme-dataset\\threads\\en\\"
    path = "{opath}{db}".format(opath=origpath, db=database)

    cols = ["contributors", "truncated",
     "text",
     "in_reply_to_status_id", "id", "favorite_count",
     "source",
     "retweeted", "coordinates", "entities", "in_reply_to_screen_name", "id_str",
     "retweet_count", "in_reply_to_user_id", "favorited",
     "retweeted_status", "user", "geo", "in_reply_to_user_id_str", "possibly_sensitive",
     "lang", "created_at", "in_reply_to_status_id_str", "place"]
    df = pd.DataFrame(columns=cols)

    with open("user-news.csv", 'w', encoding="utf-8", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['id', 'tweet-id-rtd'])
        writer.writeheader()
        rows = []
        for subdir, dirs, files in os.walk(path):
            for filename in files:
                if filename.endswith("retweets.json"):

                    fpath = os.path.join(subdir, filename)
                    #print(os.path.join(subdir, filename))
                    f = open(fpath, "r")
                    for line in f:
                        dict = json.loads(line)
                        #print(dict['user']['id'], dict['retweeted_status']['id'])
                        towrite = {'id': dict['user']['id'], 'tweet-id-rtd': dict['retweeted_status']['id']}
                        rows.append(towrite)
                    #dict = json.load(f)
                    #dict['text'] = re.sub(r"[\n\t]*", "", dict['text'])
                    #dict['text'] = dict['text'].translate(str.maketrans('','', string.punctuation))
                    #print(dict['user']['id'], dict['media']['id_str'])
                    #rows.append(dict['user']['id'])

                    #print(dict)
                    #temp = pd.DataFrame.from_dict(dict)
                    #print(temp['id'])
                    #df = df.append(temp, ignore_index=True)
                    #print(dict.keys())
                    f.close()
            #print(len(rows))
        writer.writerows(rows)
    csvfile.close()

    #f = open(path, "r")

    #f.close()

    return 0
# W is m x n (users x articles)

#initialize W as np.zeros(m, n)

readRetweets("charliehebdo")