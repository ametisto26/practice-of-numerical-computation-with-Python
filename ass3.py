# -*- coding: utf-8 -*-
"""
assignment 3
"""
import math

"""
3-1
"""
# 解を求める方程式 f(x)=0
def f(x):
    return x**3 - 10
 
# 導関数
def df(x):
    return 3*x**2


# ニュートン法
def newton_method(a, eps,l):
    for i in range(1000):
        l.append(a)
          # 漸化式
        ah = a - f(a)/df(a)
        # 収束条件(近似解の変化が十分小さい)を満たせば計算終了
        if abs(ah - a) < eps:break
        #　近似解の更新
        a = ah      
    return a, i, l
    

def main():
    a , i ,l= newton_method(2, 1e-10,[])
    print("解: x =",a ,"(計算回数:", i+1, ")")
    print("項の推移\n",l)
    x = l
    j = 0
    y1,y2,y3 = [],[],[]
    while j < i :
        y1.append(abs((x[j+1]-a)/((x[j]-a)**2)))
        y2.append(abs((x[j+1]-a)/((x[j]-a)**2.5)))
        y3.append(abs((x[j+1]-a)/((x[j]-a)**3)))
        j += 1
    print("(2次)\n",y1)
    print("(2.5次)\n",y2)
    print("(3次)\n",y3)
    print("求められた数値解の3乗の値：",a*a*a)
    
    
if __name__ == '__main__':
    main()

"""
3-2 (i)
"""
# 解を求める方程式 f(x)=0
def f(x):
    return x**3 - x**2 - 8*x + 12
 
# 導関数
def df(x):
    return 3*x**2 - 2*x - 8

# ニュートン法
def newton_method(a, eps,l):
    for i in range(1000):
        l.append(a)
          # 漸化式
        ah = a - f(a)/df(a)
        # 収束条件(近似解の変化が十分小さい)を満たせば計算終了
        if abs(ah - a) < eps:break
        #　近似解の更新
        a = ah      
    return a, i, l
    

def main():
    a , i ,l= newton_method(3, 1e-10,[])
    print("解: x =",a ,"(計算回数:", i+1, ")")
    print("項の推移\n",l)
    x = l
    j = 0
    y1,y2,y3 = [],[],[]
    while j < i :
        y1.append(abs((x[j+1]-a)/((x[j]-a)**1)))
        y2.append(abs((x[j+1]-a)/((x[j]-a)**1.5)))
        y3.append(abs((x[j+1]-a)/((x[j]-a)**2)))
        j += 1
    print("(1次)\n",y1)
    print("(1.5次)\n",y2)
    print("(2次)\n",y3)
    print("数値解をf(x)に代入した結果",f(a))

    
if __name__ == '__main__':
    main()


"""
3-2 (ii)
"""
# 解を求める方程式 f(x)=0
def f(x):
    return math.sin(x) - math.tan(x)
 
# 導関数
def df(x):
    return math.cos(x) - 1 - (math.tan(x))**2

# ニュートン法
def newton_method(a, eps,l):
    for i in range(1000):
        l.append(a)
          # 漸化式
        ah = a - f(a)/df(a)
        # 収束条件(近似解の変化が十分小さい)を満たせば計算終了
        if abs(ah - a) < eps:break
        #　近似解の更新
        a = ah      
    return a, i, l
    

def main():
    a , i ,l= newton_method(0.1, 1e-10,[])
    print("解: x =",a ,"(計算回数:", i+1, ")")
    print("項の推移\n",l)
    x = l
    j = 0
    y1,y2,y3 = [],[],[]
    while j < i :
        y1.append(abs((x[j+1]-a)/((x[j]-a)**1)))
        y2.append(abs((x[j+1]-a)/((x[j]-a)**1.5)))
        y3.append(abs((x[j+1]-a)/((x[j]-a)**2)))
        j += 1
    print("(1次)\n",y1)
    print("(1.5次)\n",y2)
    print("(2次)\n",y3)
    print("数値解をf(x)に代入した結果",f(a))
    
if __name__ == '__main__':
    main()


"""
3-2(ii) 未使用分

import math
# 解を求める方程式 f(x)=0
def f(x):
    return math.sin(x) - math.tan(x)
 
# 導関数
def df(x):
    return math.cos(x) - 1 - (math.tan(x))**2

def d2f(x):
    return -math.sin(x) + 2*math.tan(x)+2*(math.tan(x))**3

def g(x):
    return f(x)/df(x)

def dg(x):
    return 1 - (f(x)*d2f(x))/(df(x)**2)

# ニュートン法
def newton_method(a, eps,l):
    for i in range(1000):
        l.append(a)
          # 漸化式
        ah = (a - f(a)/df(a))/2 + (a - g(a)/dg(a))/2
        # 収束条件(近似解の変化が十分小さい)を満たせば計算終了
        if abs(ah - a) < eps:break
        #　近似解の更新
        a = ah      
    return a, i, l
    

def main():
    a , i ,l= newton_method(1, 1e-10,[])
    print("解: x =",a ,"(計算回数:", i+1, ")")
    print("項の推移\n",l)
    x = l
    j = 0
    y1,y2,y3 = [],[],[]
    while j < i :
        y1.append(abs((x[j+1]-a)/((x[j]-a)**1)))
        y2.append(abs((x[j+1]-a)/((x[j]-a)**1.5)))
        y3.append(abs((x[j+1]-a)/((x[j]-a)**2)))
        j += 1
    print("(1次)\n",y1)
    print("(1.5次)\n",y2)
    print("(2次)\n",y3)
    print("数値解をf(x)に代入した結果",f(a))
    
if __name__ == '__main__':
    main()
"""