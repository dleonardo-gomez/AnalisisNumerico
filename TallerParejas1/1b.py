# coding: utf-8
# Your code here!

from sympy import *
from math import *
from numpy import*


def horner(poly, x):
    result = poly[0]
    n=len(poly)
    cont=0
    for i in range(1, n):
        result = result * x 
        if poly[i]!=0:
            result+=poly[i]
            cont+=1
        cont+=1
    print ("resultado del polinomio evaluado :" + str(result))
    return cont
    

def main():
    
    p=[7,6,-6,0,3,-4]
    x=3
    cont=horner(p, x)
    print("numero total de operaciones :"+str(cont))
    
if __name__ == "__main__":
    main()
