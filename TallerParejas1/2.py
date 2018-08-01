from sympy import *
from math import *
from numpy import*

def f(x):
    return (32-2*x)*(24-2*x)*x-1000
    
def df(x):
    return 12*x*x-224*x+768
    
def bisec(a,b):
    x = (a+b)/2
    e = abs((a-b)/2)
    while e>1e-8:
        if f(x)==0:
            return x
        if f(x)*f(a)<0:
            b=x
        else:
            a=x
        e=abs((a-b)/2)
        x=(a+b)/2
    return x
 

def main():
	x=0.0
	x1=0.0
	e=100.0
# resuelto por newton
	while e>1e-6:
		x=x1
		if df(x) != 0:
		    x1=x-f(x)/df(x)
		else:
		    x1=x-f(x)/1e-6
		e=abs(x-x1)
	
	print('Newton ' + str(x1))
	print('Resultado: ' + str(f(x1)+1000))
# resuleto por biseccion
	a=0.0
	b=5.0
	print('Bisección ' + str(bisec(a,b)))
	print('Resultado: ' + str(f(bisec(a,b))+1000))

if __name__ == "__main__":
    main()
