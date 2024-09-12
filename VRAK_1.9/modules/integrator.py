### integrator

import numpy


def biexp(halflife,A1,k1,A2,k2):
    k1=abs(k1)
    k2=abs(k2)
    exp_half=(numpy.log(2)/float(halflife))
    integral=A1/(exp_half+k1)+A2/(exp_half+k2)
    return integral


def triexp(halflife,A1,k1,A2,k2,A3,k3):
    exp_half=(numpy.log(2)/float(halflife))
    k1=abs(k1)
    k2=abs(k2)
    k3=abs(k3)
    integral=A1/(exp_half+k1)+A2/(exp_half+k2)+A3/(exp_half+k3)
    return integral
