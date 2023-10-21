def p(x):
    return (4*(x**3))-((263/8)*(x**2))+((231/4)*x)-(199/4)


# m =(a+b)/2

def beisektionsmetode(interval, a, b):
    a = a
    b = b
    for i in range(interval):
        m = (a+b)/2
        if (p(m) > 0):
            b = m
        elif (p(m) < 0):
            a = m
        print("-----",i,"-----")
        print("m: ",m)
        print("p(m): ", p(m))
        print("p(a): ", p(a))
        print("p(b): ", p(b))


beisektionsmetode(7, 6, 7)
