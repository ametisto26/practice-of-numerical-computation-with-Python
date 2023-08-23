# -*- coding: utf-8 -*-
"""
assignment 5-1
"""
#import math
import numpy as np

def naiseki(a,b):
    ans = np.sum(np.multiply(a,b))
    return ans


def solve_CG(A,b,k):
    alpha = 10
    x = np.array([[0],[0],[0],[0]])
    m = A.T * (A*x-b)
    t = -(naiseki(m,A.T*(A*x-b)))/(naiseki(m,A.T*A*m))
    x = x + t*m

    for i in range(k):
        alpha = - (naiseki(m,A.T * A * A.T*(A*x-b)))/(naiseki(m, A.T*A*m))
        m = A.T * (A*x-b) + alpha*m
        t = -(naiseki(m,A.T*(A*x-b)))/(naiseki(m,A.T*A*m))
        x = x + t*m

    return x

A = np.matrix([[1,1,1,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
b = np.array([[1],[1],[2],[1]])

print(solve_CG(A,b,1000))
