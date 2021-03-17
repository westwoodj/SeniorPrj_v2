import pandas as pd
import csv
import argparse
from utils import *

parser = argparse.ArgumentParser()
parser.add_argument('--corpus_file', default='data/doc_term_mat1.txt', help='term document matrix file')
parser.add_argument('--vocab_file', default='data/vocab1.txt', help='vocab file')
parser.add_argument('--model', default='seanmf', help='nmf | seanmf')
parser.add_argument('--max_iter', type=int, default=500, help='max number of iterations')
parser.add_argument('--n_topics', type=int, default=100, help='number of topics')
parser.add_argument('--alpha', type=float, default=0.1, help='alpha')
parser.add_argument('--beta', type=float, default=0.0, help='beta')
parser.add_argument('--max_err', type=float, default=0.1, help='stop criterion')
parser.add_argument('--fix_seed', type=bool, default=True, help='set random seed 0')
args = parser.parse_args()


def computeX(dt_mat):
    d = read_docs(args.corpus_file)
    v = read_vocab(args.vocab_file)

    n = len(d)
    t = len(v)
    X = np.zeros((n, t), dtype=np.longdouble)
    with open(dt_mat, 'r') as dtfile:
        reader = csv.reader(dtfile, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
        i = 0
        for row in reader:
            for item in row:
                X[i, int(item)] += 1
            i+=1
    print(X)
    np.save('C:\\Users\\minim\\PycharmProjects\\SeniorPrj\\results\\X.npy', X)
    np.savetxt('C:\\Users\\minim\\PycharmProjects\\SeniorPrj\\NewsEmbedding\\data\\X.csv', X, delimiter=' ', newline='\n',
               fmt='%i')
                #print(row, item)



computeX("C:\\Users\\minim\\PycharmProjects\\SeniorPrj\\NewsEmbedding\\data\\doc_term_mat1.txt")