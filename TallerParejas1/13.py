from sympy import *
from math import *
from numpy import*

res = []

def biseccion(n, raiz, a, b):
    middle = abs((a-b)/2)
    valor = 1
    res.append(a+middle)
    for x in range(0,raiz):
        valor = (a+middle) * valor

    if(a>b):
        return   
    if(len(res)>1):
        e = abs((res[len(res)-1]-res[len(res)-2])/2)
        if(e>1e-6):
            if(valor == n):
                return
            elif (valor>n):
                biseccion(n,raiz,a,b-middle)
            else:
                biseccion(n,raiz,a+middle,b)
    else:
        if(valor == n):
            return
        elif (valor>n):
            biseccion(n,raiz,a,b-middle)
        else:
            biseccion(n,raiz,a+middle,b)
            

def main():
    num = 16
    raiz = 3
    err = []
    biseccion(num, raiz, 0, num)
    
    for x in range(0,len(res)):
        print('Iteración #'+str(x)+': '+str(res[x]))
    
    for x in range(0,len(res)-1):
        err.append(res[x+1]/res[x])
    
    
    for x in range(0,len(err)):
        print('k: '+str(err[x]))

if __name__ == "__main__":
    main()
