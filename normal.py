import math
from decimal import Decimal

def norm(x,sigma, miu):
    val = (1/(sigma * math.sqrt(2*math.pi))) * math.exp((-0.5*((x-miu)/sigma)**2))
    return val

def z(x):
    return (1/math.sqrt(2*math.pi)) * math.e **(-0.5*((x)**2))

def area(b,h):
    return  b*h

def reinman(inicio, fin, pSize, sigma, miu):
    aprox = 0
    while inicio < fin:
        aprox += area(pSize,norm(inicio + (pSize/2), sigma, miu))
        inicio += pSize
    return aprox

def reinmanZ(inicio, fin, pSize):
    aprox = 0
    while inicio < fin:
        aprox += area(pSize,z(inicio + (pSize/2)))
        inicio += pSize
    return aprox

#0-3 4 decimales
print("0.0000 || ", end="")
for i in range(0,10):
  print("0.00" + str(i) + "0",end = " | ")

print("\n")
x = 0
cont = 0
print("0.0000 || ", end="")
while x < 1:
    y = Decimal(reinmanZ(-10,x,0.001))
   
    print(round(y,4),end=" | ")
    cont += 1
    if(cont== 10):
        max = Decimal(x+0.001)
        print()
        print(str(round(max,4))+" || ", end="")
        cont = 0
    x += 0.001
