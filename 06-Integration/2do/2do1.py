#
# please refer to PPT file
# for exercise
#
# Integración numérica
#
# Regla del punto medio
# Regla del trapecio
# Regla de Simpson

from math import sin, sqrt

def f(x):
    return 2*(sin(sqrt(x)))-x

a = 0
b = 1.9724

m = (a+b)/2
r2 = f(m)*(b-a)
print('Regla del punto medio: ',r2)

r3 = ((b-a)/2)*(f(a)+f(b))
print('Regla del trapecio: ',r3)

r4 = ((b-a)/6)*(f(a)+4*f(m)+f(b))
print('Regla de Simpson: ',r4)



