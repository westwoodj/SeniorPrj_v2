import pandas as pd
import csv
import io
import numpy as np
import json
import ast
import re


def makeCorpus(file):
    df = pd.read_csv(file)
    # windows-1252 encoding
    with open('data/corpus.txt', 'w', encoding="utf-8") as f:
        np.savetxt(f, df['text'], fmt="%s", delimiter='/n')
    f.close()
    return 0


def dictifyCol(val):
    ret =  ast.literal_eval(val)
    return ret

def makeB(file):
    df = pd.read_csv(file)
    #corrMat = df.corr()
    #print(corrMat)
    us = df["user"].apply(dictifyCol).to_dict()
    #test = ast.literal_eval(us[0])
    #print(test['id']) #{"follow_request_sent","profile_use_background_image","profile_text_color","default_profile_image","id","profile_background_image_url_https","verified","profile_location","profile_image_url_https","profile_sidebar_fill_color","entities","description","followers_count","profile_sidebar_border_color","id_str","profile_background_color","listed_count","is_translation_enabled","utc_offset","statuses_count","description","friends_count","location","profile_link_color","profile_image_url","following","geo_enabled","profile_banner_url","profile_background_image_url","name","lang","profile_background_tile","favourites_count","screen_name","notifications","url","created_at","contributors_enabled","time_zone","protected","default_profile","is_translator"}
    #print(us[0]['id'])
    with open('../PublishingEmbedding/publisher-news.csv', 'w', encoding="utf-8", newline='') as f:
        writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, )

        for key in us:
            #print(df["id"])
            #us[key]["id"] = re.sub(r"[\n\t]*", "", us[key]["id"])
            #df.iloc[key]["id_str"] = re.sub(r"[\n\t]*", "", df.iloc[key]["id_str"])
            writer.writerow([us[key]["id"], df.iloc[key]["id_str"]])
        #np.savetxt(f, us, fmt="%s", delimiter='/n')
    return 0

if __name__ == "__main__":
    makeB("source_tweets.csv")