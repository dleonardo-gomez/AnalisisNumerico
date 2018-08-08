from sympy import *
from math import *
from numpy import*

def main():
    x=1
    k=5
    err = []
    res = []
    
    for y in range(0,k):
        x1 = x
        x = g(x1)
        e = abs(x-x1)
        res.append(e)
        print('Iteracion #' + str(y+1) + ': '+str(x))
    
    for x in range(0,len(res)-1):
        err.append(res[x+1]/res[x])
    
    for x in range(0,len(err)):
        print('Coeficiente k# '+str(x)+': '+ str(err[x]))
               
    print('\n Aproximado = f(' + str(x) + ') = '+ str(f(x))+'\n')
    
    
def f(x):
    return 5*x-exp(x)-1


def g(x):
    return (1+exp(x))/5
    
if __name__ == "__main__":
    main()
