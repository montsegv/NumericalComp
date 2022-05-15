#
# please refer to PPT file
# for exercise
#
#
# Integración numérica
#
# Regla del punto medio
# Regla del trapecio
# Regla de Simpson


def f(x):
    return (7**-x)+3

a = -1
b = 2

r1 = f(a)*(b-a)
print('Regla del Rectángulo: ',r1)

m = (a+b)/2
r2 = f(m)*(b-a)
print('Regla del punto medio: ',r2)

r3 = ((b-a)/2)*(f(a)+f(b))
print('Regla del trapecio: ',r3)

r4 = ((b-a)/6)*(f(a)+4*f(m)+f(b))
print('Regla de Simpson: ',r4)