import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import*
import numpy as np


def f(x): return 1-(400/9.81*(3*x + ((x**2)/2))**3) * (3 + x)
a=0
b=2
e=0.00001
r=0
cuenta = 10
S=[a]
Error=[1]
relativo = [np.absolute((b-a)/(b))]
Conv = []
while relativo[r]>=e and cuenta > 0:
    cuenta = cuenta - 1
    r = r+1
    c=(a+b)/2
    print("La solución aproximada en la i-esima iteración es x=",c)
    if f(c)==0:
        print("La solución obtiene en x=",c)
    else:
        if f(a)*f(c)>0:
            a=c
        else:
            b=c
    
    Anterior = r-1
    S.append(c)
    absoluto = np.absolute(S[r]-S[Anterior])
    rela = np.absolute((S[r]-S[Anterior])/S[r])
    relativo.append(rela)
    Error.append(absoluto)
    Razon = (Error[r]/Error[1])
    Conv.append(Razon)
    print("Error absoluto =",absoluto)
    print("Error relativo =",relativo[r])
    print("Razón convergencia =",Conv)
    if cuenta == 0:
        print("***********Máxima cantidad de iteraciones alcanzada***********")
    
x = Symbol('x')
g = (1-(400/9.81*(3*x + ((x**2)/2))**3) * (3 + x))
plot(g,(x,0,2))