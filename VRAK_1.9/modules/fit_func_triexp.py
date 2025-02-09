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

def func(A1,k1,A2,k2,A3,k3,x):
    y=A1*np.exp(k1*x)+A2*np.exp(k2*x)+A3*np.exp(k3*x)
    return y


def fit_triexp(t0,t1,t3,d0,d1,d3):
    t0=float(t0)
    t1=float(t1)
    t3=float(t3)
    d0=float(d0)
    d1=float(d1)
    d3=float(d3)
    if d3==d1 or d1==d0 or d0==d3:
        d0+=0.0001
        d1+=0.0002
        d3+=0.0003
    d1lin=(((d3-d0)/(t3-t0))*t1+(d0-((d3-d0)/((t3-t0))*t0)))
    if d1<d1lin:
       d1=d1lin
       #print 'lined',d1
    if d3<0.1*d1:
       d3=0.1*d1
    if d0<0.2*d1:
       d0=0.2*d1

    if d3>d1:
        k3=-0.001
        A3=d3/(np.exp(k3*t3))
        
        x=np.array([t1,t3])
        y=np.array([d1-(A3*np.exp(k3*t1)),0.01*d3])
        A2,k2=fit_exp_linear(x,y)
        #print 'a'
        if (A2+A3)<0:
            A2=-A3
            A1=0
            k1=0
            #print 'b'
        else:
            A1=-(A2+A3)
            k1=-6
            #print 'c'
    else:
        x=np.array([t1,t3])
        y=np.array([d1,d3])
        A3,k3=fit_exp_linear(x,y)
        if k3>-0.001:
           k3=-0.001
           A3=d3/(np.exp(k3*t3))
        x=np.array([t0,t1])
        y=np.array([d0-(A3*np.exp(k3*t0)),0.01*d1])
        #print y
        A2,k2=fit_exp_linear(x,y)
        #print 'g'
        if (A2+A3)<0:
            A2=-A3
            A1=0
            k1=0
            #print 'h'
        else:
            A1=-(A2+A3)
            k1=-6
            #print 'i'
    best_plsq=np.array([A1,k1,A2,k2,A3,k3])
    return best_plsq
