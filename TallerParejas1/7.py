from sympy import *
from math import *
from numpy import*

def main():
    x1=1
    e=100
    while(e>1e-4):
        x=x1
        x1=x-df(x)/ddf(x)
        e= abs(x-x1)
        
    print(str(x1))
    


def f(x):
    return	3+3*cos(x)*cos(x)-2*(sin(x)+cos(x))


def df(x):
    h=1e-6;
    return (f(x+h)-f(x))/h


def ddf(x):
    h=1e-6
    return (df(x+h)-df(x))/h

if __name__ == "__main__":
    main()
