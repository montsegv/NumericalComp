#
#Dados: (-1,3), (0,-7), (4,7) y (5,11) estimar el polinomio interpolante
#2do
#

from re import X

p1 = (-1,3)
p2 = (0,-7)
p3 = (4,7)
p4 = (5,11)
x = float(input("Ingresa el valor de X: "))

def fn(x,p1,p2,p3,p4):
    r1=(((x-p2[0])*(x-p3[0])*(x-p4[0]))/((p1[0]-p2[0])*(p1[0]-p3[0])*(p1[0]-p4[0])))*(p1[1])
    r2=(((x-p1[0])*(x-p3[0])*(x-p4[0]))/((p2[0]-p1[0])*(p2[0]-p3[0])*(p2[0]-p4[0])))*(p2[1])
    r3=(((x-p1[0])*(x-p2[0])*(x-p4[0]))/((p3[0]-p1[0])*(p3[0]-p2[0])*(p3[0]-p4[0])))*(p3[1])
    r4=(((x-p1[0])*(x-p2[0])*(x-p3[0]))/((p4[0]-p1[0])*(p4[0]-p2[0])*(p4[0]-p3[0])))*(p4[1]) 
    return r1+r2+r3+r4

print("El valor de Y es: ", fn(x,p1,p2,p3,p4))
