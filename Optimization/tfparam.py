import numpy as np
import csv
from sklearn.model_selection import train_test_split
#import tensorflow_io as tfio
d = 10  # num features

#
alpha, beta, gamma, lmbda, eta = -5, 1e-4, 10, 0.1, 1 #lmbda because lambda functions in Python

'''
alpha and beta control social relationship and user-news engagements

gamma controls publisher-partisian contribution

eta controls the input of the linear classifier

'''

n, t = 74, 52 # news, terms
m = 19867 #numer of users
l = 46 # number of publishers
r = 59 #labeled-unlabeled boundary
#get X
X = np.load(r'C:\Users\minim\PycharmProjects\SeniorPrj\results\X.npy')

#Xtf = tf.Tensor(X, dtype=np.int32)
#get A
A = np.load(r'C:\Users\minim\PycharmProjects\SeniorPrj\results\A.npy')
#Atf = tf.Tensor(A, dtype=np.int32)

#get B
B = np.load(r'C:\Users\minim\PycharmProjects\SeniorPrj\results\B.npy')
#Btf = tf.Tensor(B, dtype=np.int32)

#get W
W = np.load(r'C:\Users\minim\PycharmProjects\SeniorPrj\results\W.npy')
#Wtf = tf.Tensor(W, dtype=np.int32)

y = np.load(r'C:\Users\minim\PycharmProjects\SeniorPrj\results\y.npy')




#get o

o = np.load(r'C:\Users\minim\PycharmProjects\SeniorPrj\results\o.npy')

#print(o.shape, o)
o = o - o.mean()
o = o / 35
o = np.reshape(o, newshape=(l,1))

#otf = tf.Tensor(o, dtype=np.int32)

#print(o.shape, o)
e = np.load(r'C:\Users\minim\PycharmProjects\SeniorPrj\results\e.npy')
c = np.random.uniform(0, 1, [m, 1])  # credibility score
e = np.reshape(e, newshape=(l, 1))
#c = np.load(r'C:\Users\minim\PycharmProjects\SeniorPrj\results\c.npy')
#print(y.shape, y)
#etf = tf.Tensor(e, dtype=np.int32)

#get yL
y = np.reshape(y, newshape=(n, 1))
#ytf = tf.Tensor(y, dtype=np.int32)

#print(y.shape, y)
#yL, yU = train_test_split(y, test_size=0.2, random_state=42)
yL = y[:r, :]  # labeled
yU = y[r:, :]  # unlabeled

#yLtf = tf.Tensor(yL, dtype=np.int32)
#yUtf = tf.Tensor(yU, dtype=np.int32)


#print(yL.shape, yL)
#print(yU.shape, yU)

#get Y
Y = A.copy()
#Ytf = tf.Tensor(Y, dtype=np.int32)

#get alpha, beta, gamma, lmbda, eta ^above

F = np.zeros([m+r, m+r])  # eq. 8
S = np.zeros([m+r, m+r])  # eq. 8
L = np.zeros([m+r, m+r])  # eq. 8

#Ftf = tf.Tensor(F, dtype=np.int32)
#Stf = tf.Tensor(S, dtype=np.int32)
#Ltf = tf.Tensor(L, dtype=np.int32)



G = np.zeros([m+r, m+r])

#Gtf = tf.Tensor(G, dtype=np.int32)


L11 = L[0:m, 0:m]
L12 = L[0:m, m:]
L21 = L[m:, 0:m]
L22 = L[m:, m:]


#L11tf = tf.Tensor(L11, dtype=np.int32)
#L12tf = tf.Tensor(L12, dtype=np.int32)
#L21tf = tf.Tensor(L21, dtype=np.int32)
#L22tf = tf.Tensor(L22, dtype=np.int32)

#norm = np.linalg.norm(B)
B_bar = B / np.sum(B,axis=1).reshape(-1, 1)  # normalized B
#B_bartf = tf.Tensor(B_bar, dtype=np.int32)

#B_bar = B / norm  # normalized B
E = np.diag(e.reshape([-1]))
I = np.diag(np.ones([d]))

#Etf = tf.Tensor(E, dtype=np.int32)
#Itf = tf.Tensor(I, dtype=np.int32)

#randomly initialize U, V, T, D, p, q

U = np.random.uniform(0, 1, [m, d])  # user embedding
V = np.random.uniform(0, 1, [t, d])  # word embedding
T = np.random.uniform(0, 1, [d, d])  # user-user correlation
D = np.random.uniform(0, 1, [n, d])  # news embedding
DL = D[:r, :]  # labeled
DU = D[r:, :]  # unlabeled
p = np.random.uniform(0, 1, [d, 1])  # mapper of labeled news embedding
q = np.random.uniform(0, 1, [d, 1])  # mapper for publisher embedding
#print("q: ", q.shape, q)

#Utf = tf.Tensor(U, dtype=np.int32)
#Vtf = tf.Tensor(V, dtype=np.int32)
#Ttf = tf.Tensor(T, dtype=np.int32)
#Dtf = tf.Tensor(D, dtype=np.int32)
#DLtf = tf.Tensor(DL, dtype=np.int32)
#DUtf = tf.Tensor(DU, dtype=np.int32)
#ptf = tf.Tensor(p, dtype=np.int32)
#qtf = tf.Tensor(q, dtype=np.int32)

'''

'''


pass