def p(x):
    return (16*x**3)-(103*x**2)+174*x-142


a = 4
b = 5
m =(a+b)/2

##print(m)
print("p(m): ",p(m))
print("p(a): ",p(a))
print("p(b): ",p(b))
if(p(m)>0):
    b=m
if(p(m)<0):
    a=m
m =(a+b)/2    
print()
print("a1: ", a)
print("b1: ", b)
print("p(m): ",p(m))
print("p(a): ",p(a))
print("p(b): ",p(b))
m =(a+b)/2
if(p(m)>0):
    b=m
if(p(m)<0):
    a=m
print()
print("a2: ", a)
print("b2: ", b)
print("p(m): ",p(m))
print("p(a): ",p(a))
print("p(b): ",p(b))
m =(a+b)/2    
print(m)
print(p(m))