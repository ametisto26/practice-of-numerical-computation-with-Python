# -*- coding: utf-8 -*-
"""
入力値をfloatとして計算する。
"""

a = input("a = ")
print("a =", a, ", type(a) =", type(a))

b = input("b = ")
print("b =", b, ", type(b) =", type(b))

print("a + b =", a + b, ", type(a + b) =", type(a + b))


a, b = float(a), float(b)

print("a + b =", a + b, ", type(a + b) =", type(a + b))
