# -*- coding: utf-8 -*-
"""
assignment 2-2
"""
import math
# 解を求める方程式 f(x)=0
def f(x):
    return math.cos(x) + (x+1)*math.exp(x)
 
# f(x)の導関数
def df(x):
    return -math.sin(x)+(x+2)*math.exp(x)

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
    a , i = newton_method(0, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
        
def main():
    a , i = newton_method(-1, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
        
def main():
    a , i = newton_method(-2, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
                
def main():
    a , i = newton_method(-3, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
        
def main():
    a , i = newton_method(-4, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
        
def main():
    a , i = newton_method(-5, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
            
def main():
    a , i = newton_method(-6, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
            
def main():
    a , i = newton_method(-7, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
        
def main():
    a , i = newton_method(-8, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()
        
def main():
    a , i = newton_method(-9, 1e-40)
    print("解: x =",a ,"(計算回数:", i+1, ")")
    
if __name__ == '__main__':
    main()



print("x1 =",-6-f(-6)/df(-6))

print(abs(-1.4633436590068039 - (-(1/2)*math.pi)))
print("相対誤差：",abs((-1.4633436590068039 - (-(1/2)*math.pi))/(-1.4633436590068039)))
print(abs(-4.744958730590032 - (-(3/2)*math.pi)))
print("相対誤差：",abs((-4.744958730590032 - (-(3/2)*math.pi))/(-4.744958730590032)))
print(abs(-7.851314826065457 - (-(5/2)*math.pi)))
print("相対誤差：",abs((-7.851314826065457 - (-(5/2)*math.pi))/(-7.851314826065457)))
