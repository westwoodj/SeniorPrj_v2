# import numpy as np
# import scipy
# import pandas as pd
# import pickle
# import os
from sklearn.metrics import classification_report
from decimal import *
from Optimization.parameters import *
import sys
import warnings
import time

if not sys.warnoptions:
    warnings.simplefilter("ignore")

#from Optimization.fakeparams import *

getcontext().prec=20
def gij(ran):
    for i in range(m):
        for j in range(r):
            G[i, j] = (W[i, j] * ((c[j]*(1 - (1 + (yL[j])) / 2)) + (1 - c[j]) * ((1 + yL[j]) / 2)))

    return G


def compute_L():

    G = gij(m+r)

    # compute F
    for i in range(m+r):
        for j in range(m+r):
            if 1 <= i+1 <= m and m+1 <= j+1 <= m+r:
                F[i, j] = G[i, j-m]
            if m+1 <= i+1 <= m+r and 1 <= j+1 <= m:
                F[i, j] = G[i-m, j]

    # compute S
    for i in range(m+r):
        S[i, i] = np.sum(F[i])
    #print("Here is L: ", S-F)

    return S - F


def update_D():
    #print("updating D")
    def pos(x):
        #print("pos: \n", x)
        return (np.abs(x) + x) * 0.5
    def neg(x):
        #print("neg: \n", x)
        return (np.abs(x) - x) * 0.5
    #print(B_bar.shape)
    #print(T.shape)
    #print(E.shape)
    #print(o.shape)
    #print(q.shape)
    #D_car_1 = B_bar.T.dot(E.T)
    Adc1 = np.dot(B_bar.T, E.T)
    Bdc1 = np.dot(Adc1,E)
    Cdc1 = np.dot(Bdc1, o)
    D_caret_1 = np.dot(Cdc1, q.T)
    #D_caret_1 = B_bar.T.dot(E.T).dot(E).dot(o).dot(q.T)
    Adc2 = np.dot(DL, p)
    Bdc2 = neg(np.dot(Adc2, p.T))
    Cdc2 = pos(np.dot(yL, p.T))
    Ddc2 = neg(np.dot(L21, U))
    Edc2 = neg(np.dot(L22, DL))

    D_caret_2 = eta * Bdc2 + eta * Cdc2 + beta * Ddc2 + beta * Edc2

    D_caret = X.dot(V) + \
              gamma * pos(B_bar.T.dot(E.T).dot(E).dot(o).dot(q.T)) + \
              gamma * neg(B_bar.T.dot(E.T).dot(E).dot(B_bar).dot(D).dot(q).dot(q.T)) + \
              np.pad(D_caret_2, ((D_caret_1.shape[0] - D_caret_2.shape[0],0),(0,0)))

    D_tilde_1 = beta*pos(L21.dot(U)) + beta*pos(L22.dot(DL)) + eta*pos(DL.dot(p).dot(p.T)) + eta*neg(yL.dot(p.T))
    D_tilde = D.dot(V.T.dot(V)) + \
              lmbda*D + \
              gamma*pos(B.T.dot(E.T).dot(E).dot(B_bar).dot(D).dot(q).dot(q.T)) + \
              gamma*neg(B_bar.T.dot(E.T).dot(E).dot(o).dot(q.T)) + \
              np.pad(D_tilde_1, ((D.shape[0] - D_tilde_1.shape[0],0), (0, 0))
                     )
    divres = np.sqrt((D_caret/D_tilde))
    #print(divres, sum(divres))
    return D*np.sqrt(divres)

def update_U():
    def pos(x):
        return (np.abs(x) + x) * 0.5
    def neg(x):
        return (np.abs(x) - x) * 0.5
    ya = Y*A
    Auc = np.dot((ya), U)
    Buc = np.dot(Auc, T.T)
    Cuc = np.dot((ya).T, U)
    Duc = np.dot(Cuc, T)
    Euc = neg(np.dot(L11, U))
    Fuc = neg(L12.dot(DL))
    U_caret = alpha*Buc + alpha*Duc + beta*Euc + beta*Fuc

    Aut = np.dot(U, T)
    But = np.dot(Aut, U.T)
    Cut = np.dot(alpha*(Y*But), U)
    Dut = np.dot(Cut, T.T)
    Eut = np.dot(alpha*((Y*But).T), U)
    Fut = np.dot(Eut, T)

    U_tilde = Dut + Fut + lmbda*U + beta*pos(L11.dot(U)) + beta*pos(L12.dot(DL))
    #print(np.isfinite(U_caret).all(), np.isfinite(U_tilde).all())
    #print(np.isfinite(U).all())
   # print((U_caret >= 0).all(), (U_tilde >= 0).all())
    '''step = np.sqrt(U_caret/U_tilde)
    if np.isnan(step).any():
        print("nan error!")
        badItems = np.where(np.isnan(step))
        print("bad inputs at: "+str(badItems))
        print("bad  input values: (caret, tilde) ", str(U_caret[np.isnan(step)]), str(U_tilde[np.isnan(step)]))
        raise Exception("unexpected nan value in sqrt step!!")'''
    divres = np.divide(U_caret, U_tilde, out=np.zeros_like(U_caret), where=U_tilde!=0)
    return U*np.sqrt((divres))

def update_V():
    return V * np.sqrt(X.T.dot(D)/(V.dot(D.T).dot(D) + lmbda * V))

def update_T():
    return T * np.sqrt(alpha * U.T.dot(Y * A).dot(U) / ( alpha * U.T.dot(Y * (U.dot(T).dot(U.T))).dot(U) + lmbda * T))

def update_p():
    return (eta / (eta * DL.T.dot(DL) + lmbda * I)).dot(DL.T).dot(yL)

def update_q():
    return (eta / (eta * D.T.dot(B_bar.T).dot(E).dot(B_bar).dot(D) + lmbda * I)).dot(D.T).dot(B_bar.T).dot(E).dot(o)

def compute_yU():
    #print(DU.dot(p))
    #print(sum(DU.dot(p)))
    return np.sign(DU.dot(p))#, out=np.zeros_like(DU.dot(p)), where=abs(DU.dot(p))<1)

L[:,:] = compute_L()
steps = 1000
start = time.time()
for _ in range(steps):

    D[:,:] = update_D()
    U[:,:] = update_U()
    V[:,:] = update_V()
    T[:,:] = update_T()
    p[:,:] = update_p()
    q[:,:] = update_q()
    if _ % 10 == 0:
        end = time.time()
        print(_, "time: ", str((end-start)/60.0))
        yU_pred = compute_yU()
        start = time.time()
        report = classification_report(y_true=[[0], [-1], [-1], [0], [0], [0], [-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1]], y_pred=yU_pred)
        print("predicted yU:\n", np.reshape(yU_pred, newshape=(len(yU),)))
        print(report)

        #np.savetxt()


yU_pred = compute_yU()
print(classification_report(y_true=[[0], [-1], [-1], [0], [0], [0], [-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1]], y_pred=yU_pred))

print(yU_pred)