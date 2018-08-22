import math

def interseccion(x0,x1,e):
    x2 = x1 - (diff(x1)/(diff(x1)-diff(x0)))*(x1-x0)
    print(x2)
    if( diff(x2)*diff(x1) < 0):
        x1 = x2
        x0 = x1
    else:
        x1 = x2
        x0 = x0
        
    print (x0)
    print (x1)
        
    return 0, 0 

def f(x):
    return math.log(x+2)
    
def g(x):
    return math.sin(x)
    
def diff(x):
    return f(x)-g(x)
    
def main():
    e = 1;
    f(0)
    f(10)
#    while (e>1e-7):
    x, e = interseccion(0,5,e)
    
    
if __name__ == "__main__":
    main()
