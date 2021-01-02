# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 22:06:28 2021

@author: Danilo
"""
from numpy import *
import numpy as np 

# Entrys

n = 3
x = np.array([0.1,0.2,0.3,0.4])
z = np.zeros(8)
Q = np.zeros((8,8))
fx = np.array([-0.62049958,-0.28398668,0.00660095,0.24842400])
dfx = np.array([3.58502082,3.14033271,2.66668043,2.16529366])

def Hermite(n,x,z,Q,fx,dfx):
    for i in range(n+1): # Although the algorithm indicates from 0 to n, in python it is up to n + 1
        z[2*i] = x[i]
        z[2*i+1] = x[i]
        Q[2*i,0] = fx[i]
        Q[2*i+1,0] = fx[i]
        Q[2*i+1,1] = dfx[i]
        if(i != 0):
            Q[2*i,1] = (Q[2*i,0]-Q[2*i-1,0])/(z[2*i]-z[2*i-1])
    for i in range(2,2*n+2,1):
        for j in range(2,i+1,1):
            Q[i,j] = (Q[i,j-1]-Q[i-1,j-1])/(z[i]-z[i-j])

    for i in range(8): 
        for j in range(8):
            if(i == j):
                print(Q[i,j]) # # Print the output Q
    # Some indexes were changed in "for i in range" to adapt the notation used by python

Hermite(n,x,z,Q,fx,dfx)