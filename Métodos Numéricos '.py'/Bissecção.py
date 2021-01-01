# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 08:51:16 2020

@author: Danilo
"""

from numpy import *
import numpy as np 

# Entry

# Enter the interval [a, b] in the variables below.
a = 1
b = 2

TOL = 0.0001 # TOL indicates tolerance. In other words, the sequence of iterates is performed to the extent
             # between the interval is less than the given tolerance.
Max_iter = 100 # Indicates the maximum number of iterations that can be performed by the method.

f = lambda x: x**3+4*x**2-10 # The function of a single variable to be applied by the Bisection method is defined.

# Bisection Method

i = 1
FA = f(a)

while(i < Max_iter):
    p = a+(b-a)/2
    FP = f(p)
    if(FP == 0 or (b-a)/2 < TOL):
        print("Approximate solution:", p)
        break;
    i = i+1
    if(FA*FP > 0):
        a = p
        FA = FP
    else:
        b = p
        
import matplotlib.pyplot as plt  

# The result presented in the approximate solution, can be visualized through the use of the graphical view.

# Two meshes are defined: the first is defined arbitrarily while the second is defined close to the approximate solution.
x1 = np.linspace(-2,2)
x2 = np.linspace(1.2,1.5)

plt.figure()
plt.subplot()
plt.plot(x1, f(x1))  
plt.title('Graph of f(x) = x**3+4*x**2-10')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()

plt.figure()
plt.subplot()
plt.plot(x2, f(x2))  
plt.title('Graph of f (x) = x ** 3 + 4 * x ** 2-10 in an interval close to the root.')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.grid()
plt.show()