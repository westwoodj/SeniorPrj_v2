import numpy as np
import pandas as pd




def makeRealB(file):
    df = pd.read_csv(file)
    P, A = []
    for line in df:
        if df.iloc[line] not in P:
            P.append(df.iloc[line])

        read publisher and article
        if publisher not in list P
            add publisher to list P
        if article not in list A
            add article to list A
        also have list of publisher articles AP,
        go through lists P and A, if Pi published Aj, set Bij to 1, else 0
    #normalize/indicize publishers and articles
    #dictionary of publishers with articles they have posted.
