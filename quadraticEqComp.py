# -*- coding: utf-8 -*-
"""
実数係数2次方程式
"""
import math
import cmath

print('ax^2 + bx + c = 0')
a = input('0以外の実数 a = ')
b = input('実数 b = ')
c = input('実数 c = ')

a, b, c = float(a), float(b), float(c)

D = b * b - 4 * a * c

if (D > 0):
    print(f'x = {(- b + math.sqrt(D)) / (2 * a)},  {(- b - math.sqrt(D)) / (2 * a)}')
elif (D == 0):
    print(f'x = {(- b) / (2 * a)}')
else:
    print(f'x = {(- b + cmath.sqrt(D)) / (2 * a)},  {(- b - cmath.sqrt(D)) / (2 * a)}')
