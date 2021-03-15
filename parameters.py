import numpy as np

d = 10  # num features

# buzzfeed
alpha, beta, gamma, lmbda, eta = 1e-4, 1e-5, 1, 0.1, 1 #lmbda because lambda functions in Python

# # politifact
# alpha, beta, gamma, lmbda, eta = 1e-5, 1e-4, 10, 0.1, 1


# should be replaced by real data later

#build a system to collect number of users, publishers, and


n, t = 74, 688  # news, words
m = 152  # users #need total number of users - publishers
l = 20  # publisher #number of publishers for source tweets
r = 146  # labeled-unlabeled boundary #number of labeled news sources
X = np.random.random_integers(0, 50, [n, t])  # news content
A = np.random.random_integers(0,  1, [m, m])  # users relation
B = np.random.random_integers(0,  1, [l, n])  # news publisher relation
W = np.random.random_integers(0,  1, [m, n])  # user news relation
y = np.random.choice([-1, 1], n).reshape([n, 1])  # news label
o = np.random.random_integers(-1, 1, [l, 1])  # partisan label
c = np.random.uniform(0, 1, [m, 1])  # credibility score
e = np.random.random_integers(0,  1, [l, 1])  # partisan bias label mask

yL = y[:r, :]  # labeled
yU = y[r:, :]  # unlabeled
Y = np.zeros([m,m])
Y[A==1] = 1
F = np.zeros([m+r, m+r])  # eq. 8
S = np.zeros([m+r, m+r])  # eq. 8
L = np.zeros([m+r, m+r])  # eq. 8
L11 = L[0:m, 0:m]
L12 = L[0:m, m:]
L21 = L[m:, 0:m]
L22 = L[m:, m:]
B_bar = B / np.sum(B,axis=1).reshape(-1, 1)  # normalized B
E = np.diag(e.reshape([-1]))
I = np.diag(np.ones([d]))

# randomly initialization
U = np.random.uniform(0, 1, [m, d])  # user embedding
V = np.random.uniform(0, 1, [t, d])  # word embedding
T = np.random.uniform(0, 1, [d, d])  # user-user correlation
D = np.random.uniform(0, 1, [n, d])  # news embedding
DL = D[:r, :]  # labeled                                                            #are these two supposed to be here
DU = D[r:, :]  # unlabeled                                                          # ....
p = np.random.uniform(0, 1, [d, 1])  # mapper of labeled news embedding
q = np.random.uniform(0, 1, [d, 1])  # mapper for publisher embedding

pass