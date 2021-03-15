import csv
import pandas as pd
import json
import os
import re


def readDB(database):

    origpath = "C:\\Users\\minim\\OneDrive\\Desktop\\pheme rumors\\pheme-rumour-scheme-dataset\\threads\\en\\"
    path = "{opath}{db}".format(opath=origpath, db=database)
    #cols = ['contributors', 'truncated', 'text', 'in_reply_to_status_id', 'id', 'favorite_count',
    #                           'source', 'retweeted', 'coordinates', 'entities', 'in_reply_to_screen_name', 'id_str',
    #                           'retweet_count', 'in_reply_to_user_id', 'favorited', 'user', 'geo',
    #                           'in_reply_to_user_id_str', 'possibly_sensitive', 'lang', 'created_at', 'filter_level',
    #                          'in_reply_to_status_id_str', 'place', 'metadata', 'extended_entities']

    #dicttemp['user']['id'] is the retweeters id, replace user with 'retweeted_status' to get source user id
    cols = {"contributors", "truncated", "text", "in_reply_to_status_id", "id", "favorite_count", "source", "retweeted",
            "coordinates", "entities", "in_reply_to_screen_name", "id_str", "retweet_count", "in_reply_to_user_id",
            "favorited", "retweeted_status", "user", "geo", "in_reply_to_user_id_str", "possibly_sensitive", "lang",
            "created_at", "in_reply_to_status_id_str", "place", "extended_entities"}

    df = pd.DataFrame(columns=cols)
    with open("retweets.csv", 'w', encoding="utf-8", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=cols)
        writer.writeheader()
        rows = []
        for subdir, dirs, files in os.walk(path):
            for filename in files:
                if filename == ("retweets.json"):
                    fpath = os.path.join(subdir, filename)
                    print(os.path.join(subdir, filename))
                    f = open(fpath, "r", encoding="utf-8")
                    dict = json.load(f)
                    dict['text'] = re.sub(r"[\n\t]*", "", dict['text'])
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


if __name__ == "__main__":
    readDB("charliehebdo")