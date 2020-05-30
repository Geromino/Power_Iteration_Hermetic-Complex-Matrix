#!/usr/bin/env python3
import numpy as np
# function to calculate the Rayleigh quotient
def rayleigh_quotient(A,x):
    return np.dot(x, np.dot(A, x))/np.dot(x,x)
# function to normalise a vector
def normalise(x,eps=1e-10):
    N = np.sqrt(np.sum(abs(x)**2))
    if N < eps: # in case it is the zero vector!
        return x
    else:
        return x/N
        
A = np.array([[4, -1j, 2],
[1j, 2, 2+7j],
[2, 2-7j, -2]])
# choose the starting vector
x = normalise(np.array([1, 1, 1]))
RQnew = rayleigh_quotient(A,x)
print (RQnew)
RQold = 0
