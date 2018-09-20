print("oi, mundo")
print ("oi, novamente")

import math
a=int(input("informe valor de a: "))
b=int(input("informe valor de b: "))
c=int(input("informe valor de c: "))
delta=b*b-4*a*c
print("delta: ", delta)
if delta >= 0:
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b+math.sqrt(delta))/(2*a)
    print("raiz x1: ",x1)
    print("raiz x2: ", x2)
else:
    print("nao existe raizes reais")





