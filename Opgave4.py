from sympy import *
x = symbols('x')
#diff((4*(x**3))-((167/4)*(x**2))+((151/2)*x)-(135/2)) til at finde fprime

def f(x):
    return (4*(x**3))-((167/4)*(x**2))+((151/2)*x)-(135/2)
def fprime(x):
    return 12*x**2 - 83.5*x + 75.5

x0=9
def F(n):
    if n==0:
        return x0
    else:
        return (F(n-1)-f(F(n-1))/fprime(F(n-1)))


for i in range(20): #den er langsom, men den får allerede det rigtige svar ved f5 
    print("F",i,": ",F(i))