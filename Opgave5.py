import numpy as np
from sympy import *
x = symbols('x')
print(diff(sin(x)-((3*x)/10)))

def f(x):
    return np.sin(x)-((3*x)/10)
def f_deriv(x):
    return np.cos(x) - 3/10

x0=np.pi
def F(n):
    if n==0:
        return x0
    else:
        return (F(n-1)-f(F(n-1))/f_deriv(F(n-1)))


for i in range(14): #den er langsom, men den får allerede det rigtige svar ved f5 
    print("F",i,": ",F(i))
print(f(2.356441149856161))