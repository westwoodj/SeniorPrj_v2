import numpy as np
import pandas as pd
import csv



U = np.load('C:\\Users\\minim\\PycharmProjects\\SeniorPrj\\InteractionEmbedding\\users.npy')
df = pd.read_csv('C:\\Users\\minim\\PycharmProjects\\SeniorPrj\\PublishingEmbedding\\publisher-news.csv', header=0)
P = df['publisher'].to_numpy()

allup = np.concatenate((U, P), axis=0)

np.save('C:\\Users\\minim\\PycharmProjects\\SeniorPrj\\InteractionEmbedding\\usersandpubs.npy', allup)

