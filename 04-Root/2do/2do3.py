#Obtener la raiz de la funcion e^(2-x)-7x=0
#2do
#Método de sustitución sucesiva
#
#import matplotlib.pyplot as plt
from math import exp
from re import X

def fn(x):
    return exp(2-x)-7*(x)

def f2(x):
    return -exp(2-x)/-7

x0 = 1.055
x1 = -exp(2-x0)/-7

print("X1 = ",x1)

x2 = -exp(2-x1)/-7
print('x2 = ',x2)

x3 = -exp(2-x2)/-7
print("x3 = ",x3)

x4 = -exp(2-x3)/-7
print("x4 = ",x4)

x5 = -exp(2-x4)/-7
print("x5 = ",x5)

x6 = -exp(2-x5)/-7
print("x6 = ",x6)

x7 = -exp(2-x6)/-7
print("x7 = ",x7)

x8 = -exp(2-x7)/-7
print("x8 = ",x8)

x9 = -exp(2-x8)/-7
print("x9 = ",x9)

x10 = -exp(2-x9)/-7
print("x10 = ",x10)

print('La raiz de e^(2-x)-7x=0 es:  ',x10)
