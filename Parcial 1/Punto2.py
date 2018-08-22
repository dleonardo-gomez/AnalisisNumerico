import math

def interseccion(x0,x1,e):
    
    error = 1.0
    while(error > e):
        x2 = x1 - (diff(x1)/(diff(x1)-diff(x0)))*(x1-x0)
        if( diff(x2)*diff(x1) < 0):
            x1 = x1
            x0 = x2
        else:
            x1 = x2
            x0 = x0
        error = abs((f(x2) - g(x2)))
        
        print("Error: "+str(error))
        print(g(x2))
        print(f(x2))
   
    return 0, 0 

def f(x):
    return math.log(x+2)
    
def g(x):
    return math.sin(x)
    
def diff(x):
    return f(x)-g(x)
    
def main():
    interseccion(-1.99,0,1e-7)
    
    
if __name__ == "__main__":
    main()
