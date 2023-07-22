# -*- coding: utf-8 -*-
"""
ガウス積分の計算
"""
import numpy as np

#被積分関数
def func(x):
    return np.exp(- (x ** 2)) / np.sqrt(np.pi)

#定積分の近似
def integration(x_left, x_right, function, num_part):
    sumR = 0
    h = (x_right - x_left) / num_part
    x = x_left
    x_next = x + h
    
    for i in range(num_part):
        sumR += function((x + x_next) / 2) * h
        x = x_next
        x_next += h
        
    return sumR


#定積分の実施と出力
a = - 0.1
b, n = -a, 1000
print(f'integral[{a:f}, {b:f}] : {integration(a, b, func, n):40.30e}]')

a = - 0.6
b, n = -a, 1000
print(f'integral[{a:f}, {b:f}] : {integration(a, b, func, n):40.30e}]')

a = - 1
b, n = -a, 1000
print(f'integral[{a:f}, {b:f}] : {integration(a, b, func, n):40.30e}]')
        
a = - 1.5
b, n = -a, 1000
print(f'integral[{a:f}, {b:f}] : {integration(a, b, func, n):40.30e}]')
        
a = - 2
b, n = -a, 1000
print(f'integral[{a:f}, {b:f}] : {integration(a, b, func, n):40.30e}]')

a = - 2.5
b, n = -a, 1000
print(f'integral[{a:f}, {b:f}] : {integration(a, b, func, n):40.30e}]')
        
a = - 3
b, n = -a, 1000
print(f'integral[{a:f}, {b:f}] : {integration(a, b, func, n):40.30e}]')
        
a = - 3.5
b, n = -a, 1000
print(f'integral[{a:f}, {b:f}] : {integration(a, b, func, n):40.30e}]')
        
a = - 4
b, n = -a, 1000
print(f'integral[{a:f}, {b:f}] : {integration(a, b, func, n):40.30e}]')
        
a = - 4.5
b, n = -a, 1000
print(f'integral[{a:f}, {b:f}] : {integration(a, b, func, n):40.30e}]')

a = - 5
b, n = -a, 1000
print(f'integral[{a:f}, {b:f}] : {integration(a, b, func, n):40.30e}]')
        
a = - 10
b, n = -a, 1000
print(f'integral[{a:f}, {b:f}] : {integration(a, b, func, n):40.30e}]')

a = - 15
b, n = -a, 1000
print(f'integral[{a:f}, {b:f}] : {integration(a, b, func, n):40.30e}]')
        
a = - 20
b, n = -a, 1000
print(f'integral[{a:f}, {b:f}] : {integration(a, b, func, n):40.30e}]')
        
a = - 30
b, n = -a, 1000
print(f'integral[{a:f}, {b:f}] : {integration(a, b, func, n):40.30e}]')
        
a = - 40
b, n = -a, 1000
print(f'integral[{a:f}, {b:f}] : {integration(a, b, func, n):40.30e}]')
        
a = - 50
b, n = -a, 1000
print(f'integral[{a:f}, {b:f}] : {integration(a, b, func, n):40.30e}]')
