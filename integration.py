# -*- coding: utf-8 -*-
"""
定積分の計算
"""
import numpy as np

#被積分関数
def func(x):
    return 5 * np.sqrt(1 - 0.8 ** 2 * x ** 2) / np.sqrt(1 - x ** 2)

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
a, b, n = 0, 0.8, 100
print(f'integral[{a:f}, {b:f}] : {integration(a, b, func, n):40.30e}]')
        
a, b, n = 0, 0.8, 300
print(f'integral[{a:f}, {b:f}] : {integration(a, b, func, n):40.30e}]')
