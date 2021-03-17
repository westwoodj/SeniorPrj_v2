import numpy as np
import csv

d = 10  # num features

# buzzfeed
alpha, beta, gamma, lmbda, eta = 1e-4, 1e-5, 1, 0.1, 1 #lmbda because lambda functions in Python



n, t = 74, 52 # news, terms
m = 19867 #numer of users
l = 46 # number of publishers
r = 59 #labeled-unlabeled boundary
#get X
X = np.load(r'C:\Users\minim\PycharmProjects\SeniorPrj\results\X.npy')


#get A
A = np.load(r'C:\Users\minim\PycharmProjects\SeniorPrj\results\A.npy')

#get B
B = np.load(r'C:\Users\minim\PycharmProjects\SeniorPrj\results\B.npy')

#get W
W = np.load(r'C:\Users\minim\PycharmProjects\SeniorPrj\results\W.npy')

y = np.load(r'C:\Users\minim\PycharmProjects\SeniorPrj\results\y.npy')




#get o

o = np.load(r'C:\Users\minim\PycharmProjects\SeniorPrj\results\o.npy')
#print(o.shape, o)
o = np.reshape(o, newshape=(l,1))
#print(o.shape, o)

e = np.load(r'C:\Users\minim\PycharmProjects\SeniorPrj\results\e.npy')
c = np.random.uniform(0, 1, [m, 1])  # credibility score
e = np.reshape(e, newshape=(l, 1))
#c = np.load(r'C:\Users\minim\PycharmProjects\SeniorPrj\results\c.npy')
#print(y.shape, y)

#get yL
y = np.reshape(y, newshape=(n, 1))
#print(y.shape, y)

yL = y[:r, :]  # labeled
yU = y[r:, :]  # unlabeled
#print(yL.shape, yL)
#print(yU.shape, yU)

#get Y
Y = A.copy()

#get alpha, beta, gamma, lmbda, eta ^above

F = np.zeros([m+r, m+r])  # eq. 8
S = np.zeros([m+r, m+r])  # eq. 8
L = np.zeros([m+r, m+r])  # eq. 8

G = np.zeros([m+r, m+r])

L11 = L[0:m, 0:m]
L12 = L[0:m, m:]
L21 = L[m:, 0:m]
L22 = L[m:, m:]
#norm = np.linalg.norm(B)
B_bar = B / np.sum(B,axis=1).reshape(-1, 1)  # normalized B
#B_bar = B / norm  # normalized B
E = np.diag(e.reshape([-1]))
I = np.diag(np.ones([d]))
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

'''

'''


pass