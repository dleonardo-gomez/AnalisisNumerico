from sympy import *
from math import *
from numpy import*

def main():
    x=1
    k=5
    err = []
    
    for y in range(0,k):
        x1 = x
        x = g(x1)
        e = abs(x-x1)
        err.append(e)
        print('Iteracion #' + str(y+1) + ': '+str(x))
    
        
    print('Aproximado = f(' + str(x) + ') = '+ str(f(x)))
    
    val = 0
    for x in range(0,len(err)-1):
        val += err[x+1]/err[x]
    val = val / (len(err)-1)
    print('\nConvergencia 1: ' + str(val))
    
    
def f(x):
    return 5*x-exp(x)-1


def g(x):
    return (1+exp(x))/5
    
if __name__ == "__main__":
    main()
