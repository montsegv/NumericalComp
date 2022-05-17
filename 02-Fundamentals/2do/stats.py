#
# select and write 
# one of the following stat functions
#

from ast import arg
import random
from xml.etree.ElementTree import ElementTree

def sum(a,b): 
    sum = a + b
    return sum

print(sum(7,3))


def avg(num): 
    res = 0
    for _ in range(num):
        res += random.uniform(1, 50)
    return res/num

print(avg(5))

def min(argu):
    menor = argu[0]
    for elemento in argu:
        if elemento < menor:
            elemento = menor
        return menor

argument = [8,1,0,2,6,10]  
menor = min(argument)  
print('El numero menor del arreglo es: ', menor)

def max(l): pass

def range(l): pass

def std(l): pass

def mode(l): pass
