# -*- coding: utf-8 -*-
"""
assignment 2-1
"""

import math
# 解を求める方程式 f(x)=0
def f(x):
    return 24*x**3 - 10*x**2 - 3*x + 1
 
# 導関数
def df(x):
    return 72*x**2 - 20*x - 3

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
    a , i = newton_method((5-math.sqrt(79))/36, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()

        
def main():
    a , i = newton_method((5+math.sqrt(79))/36, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
    
def main():
    a , i = newton_method(-9, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()

def main():
    a , i = newton_method(-1/9, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
    
def main():
    a , i = newton_method(-1/12, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
    
def main():
    a , i = newton_method(-1/30, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
        
def main():
    a , i = newton_method(-1/100, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
    
def main():
    a , i = newton_method(0, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
    
def main():
    a , i = newton_method(13/36, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
    
def main():
    a , i = newton_method(1, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
    
def main():
    a , i = newton_method(10, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()