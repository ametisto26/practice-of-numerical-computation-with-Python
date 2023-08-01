# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 08:47:39 2023
"""

result = ""
for i in range(1, 1000):
    result = result + f"{i}"

lr = list(result)

r = ""

for i in range(1000, 2000):
    r = r + lr[i]
    
print(r)
print(lr[0])
