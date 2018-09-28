import math

def norm(x,sigma, miu):
    val = (1/(sigma * math.sqrt(2*math.pi))) * math.exp((-0.5*((x-miu)/sigma)**2))
    return val

def z(x):
    return (1/math.sqrt(2*math.pi)) * math.exp(-0.5*((x)**2))

def area(b,h):
    return  b*h

def reinman(inicio, fin, pSize, sigma, miu):
    aprox = 0
    while inicio < fin:
        aprox += area(pSize,norm(inicio + (pSize/2), sigma, miu))
        inicio += pSize
    return aprox
    
print(reinman(-50,0,1,1,0))
    