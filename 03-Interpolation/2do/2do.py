##
# refer to PPT file
# for exercise
#
#Dados: (-4,-2) y (1,5) estimar el valor de X cuando Y es 3.7
#Interpolacion lineal
#2do
#

p1=(-4,-2)
p3=(1,5)

def fn(y,p1,p3):
    a=(p3[0]-p1[0])/(p3[1]-p1[1])
    b=y-p1[1]
    return a*b+p1[0]

print("El valor de X es: ",fn(3.7,p1,p3), " cuando Y es igual a 3.7")

