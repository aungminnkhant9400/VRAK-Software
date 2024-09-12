import numpy as np


def fit_exp_linear(x,y):
   denegative=1
   if y[0]<0:
      denegative=-1
      y[0]=-y[0]
   y=np.log(y)
   k,A_log=np.polyfit(x,y,1)
   A=np.exp(A_log)*denegative
   if k>0:
      k=0
   return A, k


def solve_k1(A2,k2,t0,d0):
    A1=-(A2)
    funcd0=A2*np.exp(k2*t0)
    deltaY=d0-funcd0
    k1=-(np.log(A1/deltaY)/t0)
    return k1

def func(A1,k1,A2,k2,x):
    y=A1*np.exp(k1*x)+A2*np.exp(k2*x)
    return y


def fit_biexp(t0,t1,d0,d1):
    t0=float(t0)
    t1=float(t1)
    d0=float(d0)
    d1=float(d1)
    if d1<(0.2*d0):
       d1=0.2*d0
   
    if d1==d0:
        d1+=0.0002
    if ((d1/(np.exp(-0.005*t1)))*np.exp(-0.005*t0))>d0:
       ###(d1/(np.exp(-0.001*t1)))*np.exp(-0.001*t0), replaces D1
       k2=-0.005
       A2=d1/(np.exp(k2*t1))
       deltY=(d0-A2*np.exp(k2*t0))
       #print deltY
       #print A2
       A1=-A2
       k1=-abs((1/t0)*np.log(-deltY/A2))
       if k1>-0.05:
          k1=-0.05
    else:
       x=np.array([t0,t1])
       y=np.array([d0,d1])
       A2,k2=fit_exp_linear(x,y)
       A1=-A2
       k1=40*k2
       if k1>-0.5:
          k1=-0.5
       

    best_plsq=np.array([A1,k1,A2,k2])

    return best_plsq
