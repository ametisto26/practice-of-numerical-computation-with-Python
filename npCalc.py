# -*- coding: utf-8 -*-
"""
NumPy
"""
import numpy as np
import cmath, math

a = -4.0 # +0.0j
z = -1.0 +2.0j

print("a = ",a)
print("z = ", z)


# 平方根: NumPy
print('np.sqrt(a) = ', np.sqrt(a))
print('np.sqrt(z) = ', np.sqrt(z))

# 平方根: math, cmath
print('cmath.sqrt(a) = ', cmath.sqrt(a))  # math.sqrt はエラーになる
print('cmath.sqrt(z) = ', cmath.sqrt(z))

# べき乗: NumPy
#c = np.sqrt(a)
w = np.sqrt(z)
#print('(np.sqrt(a))^2 = ', c ** 2)
print('(np.sqrt(z))^2 = ', w ** 2)

# べき乗: math
c = cmath.sqrt(a) # math.sqrt はエラーになる
w = cmath.sqrt(z)
print('(cmath.sqrt(a))^2 = ', c ** 2)
print('(cmath.sqrt(z))^2 = ', w ** 2)

# 指数関数，三角関数，対数関数: NumPy
print('np.exp(a)   = ', np.exp(a))
print('np.sin(a)   = ', np.sin(a))
#print('np.log(a)   = ', np.log(a))
#print('np.log10(a) = ', np.log10(a))
print('np.exp(z)   = ', np.exp(z))
print('np.sin(z)   = ', np.sin(z))
print('np.log(z)   = ', np.log(z))
print('np.log10(z) = ', np.log10(z))

# 指数関数，三角関数，対数関数: math
print('math.exp(a)   = ', math.exp(a))
print('math.sin(a)   = ', math.sin(a))
print('cmath.log(a)   = ', cmath.log(a))  # math.log はエラーになる
print('cmath.log10(a) = ', cmath.log10(a))  # math.log10 はエラーになる
print('cmath.exp(z)   = ', cmath.exp(z))
print('cmath.sin(z)   = ', cmath.sin(z))
print('cmath.log(z)   = ', cmath.log(z))
print('cmath.log10(z) = ', cmath.log10(z))
