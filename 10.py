
from math import *

def fy(x):
	return (2+cos(3*x))

def f(x):
    return (exp(x)+cos(3*x))
    
def df(x):
    return (-3*sin(3*x)+exp(x))
def r(x):
	y=fy(x)
	return (sqrt(x*x+y*y))
def theta(x):
	y=fy(x)
	return atan(y/x)
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
	
	print('Newton punto en cartesianas: (' + str(x1)+','+str(fy(x1))+')')
	print('Punto en polares: (' + str(r(x1))+','+str(theta(x1))+')')

if __name__ == "__main__":
    main()