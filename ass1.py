# -*- coding: utf-8 -*-
"""
assignment 1
"""
#1
x = 0.141892
y = 0.154123
a = 0.142
b = 0.154
print(type(x),x)
print(type(y),y)
print(type(a),a)
print(type(b),b)
print(f'y-x = {y-x}') #0.012231
print('aの相対誤差')
print((a-x)/x)
print('bの相対誤差')
print((y-b)/y)
print('b-aの値')
print(b-a)
print('b-aの相対誤差')
print(((y-x)-(b-a))/(y-x))


#2
a1 = 100000000000000.0
a2 = 0.123456789
print(type(a1),a1)
print(type(a2),a2)
print('a1+a2の値')
print(type(a1+a2),a1+a2)


#3
import sys
print(sys.float_info.epsilon)

