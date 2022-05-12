#
# radious of circle inscribed in a tringle
# place here your solution code
#
#2do
import math

a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))

sum = a+b

if (c < sum):
    s = (a+b+c)*(0.5)
    rad = math.sqrt(s*(s-a)*(s-b)*(s-c))/s
    print("El semiperimetro es igual a:",s,"y El radio es igual a:",rad)
else:
    print("La suma de los valores A y B, no pueden ser menor al valor C ")
