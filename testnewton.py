from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True)

def f(x):
    return (x**3)-x-5
def fprime(x):
    return 3*(x**2)- 1

x0=2
def F(n):
    if n==0:
        return x0
    else:
        return (F(n-1)-f(F(n-1))/fprime(F(n-1)))
    
print(diff((x**3)-x-5))
print(F(0))
print(F(1))
print(F(2))
print(F(3))
print(F(4))
print(F(5))
print(F(4)==F(5))