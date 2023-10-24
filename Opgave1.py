def p(x):
    return (16*x**3)-(103*x**2)+174*x-142

#a og b er intervallet start og slut værdier
def beisektionsmetode(iterationer, a, b):
    a = a
    b = b
    for i in range(iterationer):
        m = (a+b)/2
        if (p(m) > 0):
            b = m
        elif (p(m) < 0):
            a = m
        print("m: ",m)
        print("p(m): ", p(m))
        print("p(a): ", p(a))
        print("p(b): ", p(b))
    m = (a+b)/2
    print(m)
    print(p(m))

beisektionsmetode(2, 4, 5)