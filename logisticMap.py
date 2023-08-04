# -*- coding: utf-8 -*-
"""
ロジスティック写像
"""

x = [0.7501]

for i in range(100):
    x.append(4 * x[i] * (1 - x[i]))
    
for i in range(100):
    if i % 10 == 0:
        print(i, ",", x[i])

