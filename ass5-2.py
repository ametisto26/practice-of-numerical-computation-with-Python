# -*- coding: utf-8 -*-
"""
assignment 5-2
"""
"""
5-2
(i)
"""
import math
# 解を求める方程式 f(x)=0
def f(x):
    return x**4 - 3*x**2 + 1
 
# 導関数
def df(x):
    return 4*x**3 - 6*x

# ニュートン法
def newton_method(a, eps):
    for i in range(1000):
          # 漸化式
        ah = a - f(a)/df(a)
        # 収束条件(近似解の変化が十分小さい)を満たせば計算終了
        if abs(ah - a) < eps:break
        #　近似解の更新
        a = ah      
    return a, i
    

def main():
    a , i = newton_method(5, 1e-40)
    print("解: x1 =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()

        
def main():
    a , i = newton_method(-5, 1e-40)
    print("解: x2 =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
    
def main():
    a , i = newton_method(1, 1e-40)
    print("解: x3 =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
    
def main():
    a , i = newton_method(-1, 1e-40)
    print("解: x4 =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
    
print((math.sqrt(5)+1)/2)
print((math.sqrt(5)-1)/2)



x1 = 1.618033988749895
x2 = -1.618033988749895
x3 = 0.6180339887498948
x4 = -0.6180339887498948
print("(",x1,",", 1/x1,")")
print("(",x2,",", 1/x2,")")
print("(",x3,",", 1/x3,")")
print("(",x4,",", 1/x4,")")


"""
5-2
(ii)
"""
# 解を求める方程式 f(x)=0
def f(x):
    return (1-x*x)**3 - (math.sin(x*math.pi/2))**2
 
# 導関数
def df(x):
    return -3*2*x*(1-x*x)**2 + math.pi*math.sin(x*math.pi)/2

# ニュートン法
def newton_method(a, eps):
    for i in range(1000):
          # 漸化式
        ah = a - f(a)/df(a)
        # 収束条件(近似解の変化が十分小さい)を満たせば計算終了
        if abs(ah - a) < eps:break
        #　近似解の更新
        a = ah      
    return a, i
    

def main():
    a , i = newton_method(0.4, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()

        
def main():
    a , i = newton_method(-0.4, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()


x = 0.6909024799174349 
print("x=",x,",y=", -math.sqrt(1-x*x))
print("x=",-x,",y=", math.sqrt(1-x*x))


