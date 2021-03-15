import pandas as pd
import numpy as np
import csv


'''
left biased = -35 to -6
least biased = -5 to 5
right biased = 6 to 35
'''

def trinarizeBias(classValue):
    if classValue < -5:
        return -1
    if classValue > 5:
        return 1
    else:
        return 0


def readBias(filename):
    df = pd.read_csv(filename)
    df['bias_rating'] = df['bias_rating'].apply(trinarizeBias)
    #print(df.head)
    #print(df['bias_rating'])

    return 0


if __name__ == "__main__":
    readBias("media-bias-scrubbed-results.csv")