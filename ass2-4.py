# -*- coding: utf-8 -*-
"""
assignment 2-4
"""
import math
# 解を求める方程式 f(x)=0
def f(x):
    return math.exp(x) - 2*x**2
 
# f(x)の導関数
def df(x):
    return math.exp(x) - 4*x

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
    a , i = newton_method(-1, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
            
def main():
    a , i = newton_method(-0.5, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
        
def main():
    a , i = newton_method(0, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
            
def main():
    a , i = newton_method(0.5, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
    
def main():
    a , i = newton_method(1, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
    
def main():
    a , i = newton_method(1.5, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
        
def main():
    a , i = newton_method(2, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
    
def main():
    a , i = newton_method(2.1, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
        
def main():
    a , i = newton_method(2.5, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()



print(math.cos(math.pi))
print(math.exp(-40))
print(math.exp(-20))

